from mcp.server import Server
from mcp.types import Tool, Resource
from pydantic import BaseModel
from typing import Optional, Dict, Any
from mcp_config import MCPConfig

class SetpointRequest(BaseModel):
    setpoint: float

class PlantState(BaseModel):
    irradiation: float
    power_output: float
    setpoint: Optional[float]

class DigitalTwinMCPServer:
    def __init__(self, config: MCPConfig, plant_state_callback=None):
        self.config = config
        self.server = Server("digital-twin-server")
        self.plant_state_callback = plant_state_callback
        self._register_tools_and_resources()

    def _register_tools_and_resources(self):
        @self.server.call_tool()
        async def set_plant_setpoint(request: Dict[str, Any]) -> Dict[str, Any]:
            setpoint = request.get("setpoint")
            if setpoint is None or not 0 <= setpoint <= 1:
                raise ValueError("Setpoint must be between 0 and 1")
            if self.plant_state_callback:
                await self.plant_state_callback(setpoint)
            return {"setpoint": setpoint}

        @self.server.read_resource()
        async def get_plant_state() -> Dict[str, Any]:
            if self.plant_state_callback:
                state = await self.plant_state_callback()
                return state.dict() if hasattr(state, 'dict') else dict(state)
            raise RuntimeError("Plant state callback not set")

    async def run(self):
        import mcp.server.stdio
        from mcp.server.models import InitializationOptions
        from mcp.server.lowlevel import NotificationOptions

        initialization_options = InitializationOptions(
            server_name="digital-twin-server",
            server_version="0.1.0",
            capabilities=self.server.get_capabilities(
                notification_options=NotificationOptions(),
                experimental_capabilities={},
            ),
        )
        async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
            await self.server.run(read_stream, write_stream, initialization_options) 