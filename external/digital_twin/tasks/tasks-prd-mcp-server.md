# Task List: MCP Server for Digital Twin Simulation

## Relevant Files

- `main.py` - Main FastAPI application that initializes the simulation server
- `simulation.py` - Plant simulation module that includes the MCP server implementation
- `robot_simulation.py` - Robot simulation module that includes the MCP client
- `mcp_server.py` - MCP server implementation within the plant simulation
- `mcp_client.py` - MCP client implementation within the robot simulation
- `mcp_config.py` - Configuration module for MCP server and client settings
- `requirements.txt` - Dependencies file to be updated with MCP SDK
- `tests/test_mcp_server.py` - Unit tests for MCP server functionality
- `tests/test_mcp_client.py` - Unit tests for MCP client functionality
- `tests/test_robot_simulation.py` - Unit tests for robot simulation
- `data/plant_history.json` - File for storing plant state history (created by robot)

### Notes

- Unit tests should be placed alongside the code files they are testing
- The MCP server implementation should follow the official Python SDK documentation
- The MCP client implementation should follow the official Python SDK documentation
- File-based storage will be used for the robot's store action in this phase
- Existing plant simulation logic should be preserved while adding MCP functionality
- Note: Tasks 1.0-1.5 were completed for MCP server setup. Similar setup tasks for MCP client will be part of task 3.0

## Tasks

- [x] 1.0 Set up MCP Server Infrastructure (Plant Simulation)
  - [x] 1.1 Install and configure MCP Python SDK
  - [x] 1.2 Create basic MCP server structure in `mcp_server.py`
  - [x] 1.3 Set up MCP server configuration and initialization
  - [x] 1.4 Update `requirements.txt` with necessary dependencies
  - [x] 1.5 Create basic test structure for MCP server

- [ ] 2.0 Implement Plant Entity MCP Interface
  - [ ] 2.1 Create MCP tool definition for `set_plant_setpoint`
  - [ ] 2.2 Create MCP data resource definition for `get_plant_state`
  - [ ] 2.3 Modify `simulation.py` to integrate MCP server
  - [ ] 2.4 Implement validation for setpoint values (0 to 1)
  - [ ] 2.5 Add unit tests for plant MCP interface

- [ ] 3.0 Create Robot Entity Simulation with MCP Client
  - [ ] 3.1 Create `robot_simulation.py` with basic robot structure
  - [ ] 3.2 Implement robot initialization and state management
  - [ ] 3.3 Create `mcp_client.py` for robot's MCP client implementation
  - [ ] 3.4 Implement MCP client connection to plant's MCP server
  - [ ] 3.5 Add unit tests for robot simulation and MCP client

- [ ] 4.0 Implement Robot's Store Action
  - [ ] 4.1 Create file-based storage system for plant state
  - [ ] 4.2 Implement store action in robot simulation using MCP client
  - [ ] 4.3 Add timestamp to stored plant state data
  - [ ] 4.4 Create data directory structure for storage
  - [ ] 4.5 Add unit tests for store action

- [ ] 5.0 Integrate and Test Simulation System
  - [ ] 5.1 Modify `main.py` to initialize simulation server with plant and robot
  - [ ] 5.2 Test MCP server-client communication between plant and robot
  - [ ] 5.3 Test concurrent client connections to plant's MCP server
  - [ ] 5.4 Verify plant state persistence through robot's MCP client
  - [ ] 5.5 Create integration tests for full system 