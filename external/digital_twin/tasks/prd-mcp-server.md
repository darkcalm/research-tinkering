# Product Requirements Document: MCP Server for Digital Twin Simulation

## Introduction/Overview
This feature implements a Model Context Protocol (MCP) server within the plant simulation and an MCP client within the robot simulation for a digital twin system. The system consists of two main entities: a solar power plant and a survey robot. The plant's MCP server will provide an interface for the robot's MCP client to interact with the plant's state and control capabilities.

## Goals
1. Create an MCP server within the plant simulation that exposes setpoint control and state monitoring capabilities
2. Implement an MCP client within the robot simulation to interact with the plant
3. Enable persistent storage of plant state data through the robot's MCP client
4. Maintain the existing solar power plant simulation logic

## User Stories
1. As a system operator, I want to set the plant's setpoint through the MCP server so that I can control the power output
2. As a system operator, I want to monitor the plant's state through the MCP server so that I can track its performance
3. As a system operator, I want the survey robot to store plant state data persistently so that I can analyze historical performance

## Functional Requirements
1. The plant simulation must include an MCP server that exposes a tool called `set_plant_setpoint` that accepts a float parameter between 0 and 1
2. The plant simulation's MCP server must expose a data resource called `get_plant_state` that returns the current state of the plant
3. The simulation server must initialize both the plant and robot simulations on startup
4. The robot simulation must include an MCP client that can connect to the plant's MCP server
5. The robot simulation must include a store action that uses its MCP client to persist plant state data
6. The plant simulation must maintain its existing logic for calculating power output based on irradiation and setpoint
7. The plant's MCP server must handle concurrent requests from multiple clients

## Non-Goals (Out of Scope)
1. Implementation of error handling and edge cases (to be addressed in a future phase)
2. Performance optimization and benchmarking (to be addressed in a future phase)
3. Implementation of additional plant or robot capabilities
4. User interface development
5. Authentication and authorization mechanisms

## Design Considerations
1. The MCP server and client should follow the Model Context Protocol specification
2. The plant simulation should maintain separation between its core logic and MCP server implementation
3. The robot simulation should maintain separation between its core logic and MCP client implementation
4. The robot's store action should use a simple file-based storage system for this phase
5. The plant simulation should maintain its existing API structure for state and setpoint control

## Technical Considerations
1. The implementation will use the official MCP Python SDK for both server and client
2. The plant simulation will maintain compatibility with the existing FastAPI implementation
3. The robot simulation will be implemented as a separate module with its own MCP client
4. The plant state data structure will remain unchanged from the current implementation
5. The MCP client in the robot simulation will handle reconnection logic if the connection to the plant's MCP server is lost

## Success Metrics
1. Successful integration of the MCP server within the plant simulation
2. Successful implementation of the MCP client within the robot simulation
3. Ability to set plant setpoints and retrieve plant state through the MCP interface
4. Successful implementation of the robot's store action using its MCP client
5. Maintained functionality of the existing plant simulation

## Open Questions
1. What is the preferred format for storing plant state data?
2. Should the robot simulation have any additional capabilities beyond storing plant state?
3. What is the desired frequency of plant state data storage?
4. Should there be any limits on the frequency of setpoint changes?
5. What should be the reconnection strategy for the robot's MCP client if the connection to the plant's MCP server is lost? 