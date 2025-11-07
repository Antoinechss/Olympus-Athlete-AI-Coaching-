from dataclasses import dataclass
from datetime import datetime 
from typing import Optional 

@dataclass
class Workout: 
    id: int
    name: str
    type: str
    start_date: datetime
    distance: float  
    moving_time: int
    elapsed_time: int  
    total_elevation_gain: float  
    average_speed: Optional[float] = None  
    max_speed: Optional[float] = None
    average_heartrate: Optional[float] = None
    max_heartrate: Optional[int] = None

    @classmethod
    def from_strava(cls, data: dict):
        """parses a workout data from strava"""
        return cls(
            id = data.get('id'),
            name = data.get('name'),
            type = data.get('type'),
            start_date = data.get('start_date'),
            distance = data.get('distance'),
            moving_time = data.get('moving_time'),
            elapsed_time = data.get('elapsed_time'),
            total_elevation_gain = data.get('total_elevation_gain'),
            average_speed = data.get('average_speed'),
            max_speed = data.get('max_speed'),
            average_heartrate = data.get('average_heartrate'),
            max_heartrate = data.get('max_heartrate')
        )
    
