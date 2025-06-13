import pytest
from mcp_server import DigitalTwinMCPServer
from mcp_config import MCPConfig
from pydantic import BaseModel

class MockPlantState(BaseModel):
    irradiation: float = 0.0
    power_output: float = 0.0
    setpoint: float = None

@pytest.fixture
def config():
    return MCPConfig(
        host="localhost",
        port=8000,
        debug=True
    )

@pytest.fixture
async def mock_plant_state_callback():
    state = MockPlantState()
    
    async def callback(setpoint=None):
        if setpoint is not None:
            state.setpoint = setpoint
        return state
    
    return callback

@pytest.fixture
async def mcp_server(config, mock_plant_state_callback):
    server = DigitalTwinMCPServer(config, mock_plant_state_callback)
    yield server
    server.stop()

@pytest.mark.asyncio
async def test_set_plant_setpoint(mcp_server, mock_plant_state_callback):
    # Test valid setpoint
    response = await mcp_server._handle_setpoint({"setpoint": 0.5})
    assert response["setpoint"] == 0.5
    
    # Test invalid setpoint
    with pytest.raises(ValueError):
        await mcp_server._handle_setpoint({"setpoint": 1.5})

@pytest.mark.asyncio
async def test_get_plant_state(mcp_server, mock_plant_state_callback):
    state = await mcp_server._get_plant_state()
    assert isinstance(state, MockPlantState)
    assert state.irradiation == 0.0
    assert state.power_output == 0.0
    assert state.setpoint is None

@pytest.mark.asyncio
async def test_server_initialization(config):
    server = DigitalTwinMCPServer(config)
    assert server.config == config
    assert server.plant_state_callback is None 