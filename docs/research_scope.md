# Research Scope for Proof-of-Concept (POC)

This document outlines the defined scope for the minimal proof-of-concept of the Human DER Worker Digital Twin Framework.

## 1. Operator Roles

The POC will involve two primary agent roles:

-   **Solar Farm Maintenance Dispatcher:** The main agent whose behavior is being modeled.
-   **Field Technician:** A secondary agent that exists to be the target of communication from the Dispatcher.

## 2. Core Behavior

The simulation will model one core, end-to-end behavior:

1.  The **Dispatcher** agent receives a high-priority fault alert (e.g., "inverter-fault-123").
2.  The **Dispatcher** consults a knowledge base to determine the correct action.
3.  The **Dispatcher** sends a dispatch message to the **Technician** agent.
4.  The **Technician** agent acknowledges the dispatch message.

## 3. MCP Resource Interaction

-   The "knowledge base" will be implemented as a mock JSON file located at `data/knowledge_base.json`.
-   This file will map fault codes to response strings (e.g., `"inverter-fault-123": "Dispatch Level 2 Technician"`).
-   The Dispatcher agent will use the Model Context Protocol (MCP) to query this file.

## 4. A2A/ACP Communication Scenario

-   Communication between the Dispatcher and Technician will use the Agent-to-Agent Protocol (A2A) and/or Agent Communication Protocol (ACP).
-   The **Dispatcher** will send a task message (e.g., `{ "task": "Investigate inverter-fault-123" }`).
-   The **Technician** will send back an acknowledgement message (e.g., `{ "status": "Acknowledged" }`). 