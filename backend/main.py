from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any, Optional
import uvicorn
import os
import requests
import uuid
from dotenv import load_dotenv

#API_KEY is defined in the .env file.
load_dotenv()
API_KEY = os.getenv("API_KEY")

app = FastAPI(title="Weather Data System", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage for weather data
weather_storage: Dict[str, Dict[str, Any]] = {}

class WeatherRequest(BaseModel):
    date: str
    location: str
    notes: Optional[str] = ""

class WeatherResponse(BaseModel):
    id: str

@app.post("/weather", response_model=WeatherResponse)
async def create_weather_request(request: WeatherRequest):

    #API_KEY is defined in the .env file.
    if not API_KEY:
        raise HTTPException(status_code=500, detail="Please add an API_KEY")
    
    response = requests.post(
        "http://api.weatherstack.com/historical",
        params={
            "access_key": API_KEY,
            "query": request.location,
            "historical_date": request.date
        }
    )


    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Weather API error")
    
    response_dict = response.json()
    if response_dict.get("success") is False:
        raise HTTPException(status_code=500,  detail="Weather API error")
    #generate a uuid
    unique_id = str(uuid.uuid4())
    #override using response keys if there are dupes
    weather_storage[unique_id] = {**response_dict,**request.dict()}

    return {"id": unique_id}

@app.get("/weather/{weather_id}")
async def get_weather_data(weather_id: str):
    """
    Retrieve stored weather data by ID.
    This endpoint is already implemented for the assessment.
    """
    if weather_id not in weather_storage:
        raise HTTPException(status_code=404, detail="Weather data not found")
    print(weather_storage[weather_id])
    return weather_storage[weather_id]


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)