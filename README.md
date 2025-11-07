# Strava Workout Tracker

## Overview
The Strava Workout Tracker is a Python application that retrieves the latest workouts from the Strava API and stores them in an SQLite database. This project aims to provide a simple and efficient way to manage and analyze workout data.

## Project Structure
```
strava-workout-tracker
├── src
│   ├── main.py          # Entry point of the application
│   ├── strava_api.py    # Functions to interact with the Strava API
│   ├── database.py       # SQLite database connection and operations
│   └── models
│       └── workout.py    # Defines the Workout class
├── config
│   └── settings.py       # Configuration settings for the project
├── requirements.txt       # Project dependencies
└── README.md              # Documentation for the project
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd strava-workout-tracker
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure your settings:
   - Open `config/settings.py` and add your Strava API credentials and database path.

## Usage
To run the application, execute the following command:
```
python src/main.py
```
This will initialize the application, retrieve the latest workouts from the Strava API, and store them in the SQLite database.

## Functionality
- **Retrieve Workouts**: The application connects to the Strava API to fetch the latest workout data.
- **Database Management**: Workouts are stored in an SQLite database for easy access and analysis.
- **Data Model**: The `Workout` class defines the structure of the workout records, making it easy to manage workout data.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.