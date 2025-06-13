import asyncio
from pydantic import BaseModel
from typing import Optional
import httpx

# Simple plant state model
class PlantState(BaseModel):
    irradiation: float = 0.0
    power_output: float = 0.0
    setpoint: Optional[float] = None

state = PlantState()

async def fetch_irradiation(lat: float, lon: float) -> float:
    # Example: fetch from Open-Meteo API (replace with your preferred API)
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=shortwave_radiation"
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(url)
            data = resp.json()
            print("API response")
            print("Time:", data['hourly']['time'][0], "Irradiation:", data['hourly']['shortwave_radiation'][0])
            irradiation = data['hourly']['shortwave_radiation'][0]
            return irradiation
        except Exception as e:
            print("Error fetching irradiation:", e)  # Debug: print the error
            return 0.0

async def simulation_loop(lat: float = 40.0, lon: float = -105.0, interval: int = 10):
    global state
    while True:
        irradiation = await fetch_irradiation(lat, lon)
        state.irradiation = irradiation
        # Simple power output model: power = irradiation * setpoint (if set)
        if state.setpoint is not None:
            state.power_output = irradiation * state.setpoint
        else:
            state.power_output = irradiation
        await asyncio.sleep(interval) 