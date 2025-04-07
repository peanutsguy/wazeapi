#!/usr/bin/env python3

import uvicorn
from pywaze import route_calculator
from fastapi import FastAPI
from pydantic import BaseModel

class Coordinates(BaseModel):
    lat: float
    lon: float

class RouteRequest(BaseModel):
    start: Coordinates
    end: Coordinates

async def get_time(start: str, end: str) -> float:
    """Return the travel time and distance."""

    async with route_calculator.WazeRouteCalculator() as client:
        results = await client.calc_routes(start, end)
        route_time = results[0].duration
        distance = results[0].distance
        return route_time, distance

app = FastAPI()

@app.post("/travel_time")
async def travel_time_endpoint(route_request: RouteRequest):
    start = f"{route_request.start.lat}, {route_request.start.lon}"
    end = f"{route_request.end.lat}, {route_request.end.lon}"
    travel_time, travel_distance = await get_time(start, end)
    return {"travel_time": travel_time, "travel_distance": travel_distance}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)
