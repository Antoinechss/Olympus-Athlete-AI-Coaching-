# Database layer with sqlite

import sqlite3
from typing import List, Optional
from datetime import datetime
from src.models.workout import Workout

class WorkoutDatabase:
    def __init__(self, db_path):
        self.db_path = db_path
        self.init_database()

    def init_database(self):
        """ Create the blank workouts table """
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS workouts(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                type TEXT NOT NULL, 
                start_date DATETIME NOT NULL, 
                distance REAL,
                moving_time REAL, 
                elapsed_time REAL,
                total_elevation_gain REAL,
                average_speed REAL,
                max_speed REAL,
                average_heartrate REAL,
                max_heartrate REAL)
            """)
        
        connection.commit()
        connection.close()

    def add_workout(self, workout: Workout):
        """ add the stats of a workout to the database """
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        cursor.execute("""
            INSERT OR REPLACE INTO workouts 
            (id, name, type, start_date, distance, moving_time, 
            elapsed_time, total_elevation_gain, average_speed, 
            max_speed, average_heartrate, max_heartrate)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """,
            (workout.id,
             workout.name,
             workout.type,
             workout.start_date,
             workout.distance,
             workout.moving_time,
             workout.elapsed_time,
             workout.total_elevation_gain,
             workout.average_speed,
             workout.max_speed,
             workout.average_heartrate,
             workout.max_heartrate))
        
        connection.commit()
        connection.close()
  
    def get_all(self):
        """Fetch all workouts from DB"""
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM workouts ORDER BY start_date DESC""")
        workouts_data = cursor.fetchall()

        workouts = []
        for w in workouts_data:
            act = Workout(
                id=w[0],
                name=w[1],
                type=w[2],
                start_date=w[3],
                distance=w[4],
                moving_time=w[5],
                elapsed_time=w[6],
                total_elevation_gain=w[7],
                average_speed=w[8],
                max_speed=w[9],
                average_heartrate=w[10],
                max_heartrate=w[11])
            workouts.append(act)

        connection.close()
        return workouts
    
    
