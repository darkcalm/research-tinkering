# Digital Twin Simulation

This project simulates a solar Distributed Energy Resource (DER) plant as a digital twin. It runs a background simulation loop, fetches real solar irradiation data from an API, and exposes a FastAPI interface for state queries and remote control.

## Features
- Background simulation of a solar plant
- Fetches real solar irradiation data from Open-Meteo API
- FastAPI endpoints to get plant state and send control commands
- Can be run as a background process

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the FastAPI app:
   ```bash
   uvicorn main:app --reload
   ```
3. Access the API docs at `http://localhost:8000/docs`

## Endpoints
- `GET /plant/state`: Get current plant state
- `POST /plant/setpoint`: Set the plant setpoint (controller input)

## Configuration
- Edit `main.py` to change simulation parameters (location, interval, etc.) 