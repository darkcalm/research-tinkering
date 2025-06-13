import asyncio
from fastapi import FastAPI
from pydantic import BaseModel
import simulation
from mcp_server import DigitalTwinMCPServer
from mcp_config import MCPConfig

app = FastAPI(title="Digital Twin Simulation")

class SetpointRequest(BaseModel):
    setpoint: float

async def plant_state_callback(setpoint=None):
    if setpoint is not None:
        simulation.state.setpoint = setpoint
    return simulation.state

@app.on_event("startup")
async def startup_event():
    # Start the plant simulation
    asyncio.create_task(simulation.simulation_loop())
    
    # Initialize and start MCP server
    config = MCPConfig()
    mcp_server = DigitalTwinMCPServer(config, plant_state_callback)
    await mcp_server.run()

@app.on_event("shutdown")
async def shutdown_event():
    # Cleanup will be handled by FastAPI
    pass

@app.get("/plant/state", tags=["Digital Twin"])
def get_plant_state():
    return simulation.state

@app.post("/plant/setpoint", tags=["Digital Twin"])
def set_plant_setpoint(request: SetpointRequest):
    simulation.state.setpoint = request.setpoint
    return {"setpoint": request.setpoint} 