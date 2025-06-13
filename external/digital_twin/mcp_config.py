from pydantic import BaseModel
from typing import Optional

class MCPConfig(BaseModel):
    host: str = "localhost"
    port: int = 8000
    debug: bool = False
    plant_state_update_interval: int = 10  # seconds
    robot_state_update_interval: int = 30  # seconds

    class Config:
        env_prefix = "MCP_"  # Environment variables will be prefixed with MCP_ 