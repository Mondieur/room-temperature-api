import os
import psycopg2
from dotenv import load_dotenv # .env Reader

from flask import Flask, request # Flask

from datetime import datetime
from datetime import timezone

# RoomTable.py (also include ddl, dml and so on) 
CREATE_TABLE_ROOMS = (
    "CREATE TABLE IF NOT EXISTS rooms(id SERIAL PRIMARY KEY, name TEXT);"
)

# TemperatureTable.py
CREATE_TABLE_TEMPS = (
    """CREATE TABLE IF NOT EXISTS temperatures(room_id INTEGER, temperature REAL, 
    date TIMESTAMP, FOREIGN KEY(room_id) REFERENCES rooms(id) ON DELETE CASCADE);"""
)

INSERT_ROOM_RETURN_ID = "INSERT INTO rooms (name) VALUES (%s) RETURNING id;"
INSERT_TEMP = "INSERT INTO temperatures(room_id, temperature, date) VALUES (%s, %s, %s);"

GLOBAL_NUMBER_OF_DAYS = "SELECT COUNT(DISTINCT DATE(date)) AS days from temperatures;" # counts how many different dates we have persisted
GLOBAL_AVG = "SELECT AVG(temperature) as average FROM temperatures;"

load_dotenv() # Reads the .env file

app = Flask(__name__)
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)

@app.get("/")
def home():
    return "Hello, World!"

@app.post("/api/room")
def create_room():
    data = request.get_json()
    name = data["name"]
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_TABLE_ROOMS)
            cursor.execute(INSERT_ROOM_RETURN_ID, (name,))
            room_id = cursor.fetchone()[0]
    return {"id" : room_id, "message": f"Room {name} created."}, 201


@app.post("/api/temperature")
def add_temperature():
    data = request.get_json()
    temperature = data["temperature"]
    room_id = data["room"]
    try:
        date = datetime.strptime(data["date"], "%m-%d-%Y %H:%M:%S")
    except KeyError:
        date = datetime.now(timezone.utc)

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_TABLE_TEMPS)
            cursor.execute(INSERT_TEMP, (room_id, temperature, date))
    
    return {"message": "Temperature added."}, 201

@app.get("/api/average")
def get_global_avg():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(GLOBAL_AVG)
            average = cursor.fetchone()[0]
            cursor.execute(GLOBAL_NUMBER_OF_DAYS)
            days = cursor.fetchone()[0]

    return {"average": round(average, 2), "days": days}