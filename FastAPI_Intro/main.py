from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

sensor_readings: list[dict] = [
    {
        "id": 1,
        "sensor": "temperature",
        "content": 21.0,
        "date_timestamp": "Sept 24, 2026, 11:30"
    },
    {
        "id": 2,
        "sensor": "lux",
        "content": 100,
        "date_timestamp": "Sept 24, 2026, 11:35"
    }
]

@app.get("/", include_in_schema = False)
@app.get("/sensor_readings", include_in_schema = False)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"readings": sensor_readings})

@app.get("/api/sensor_readings")
def get_sensor_readings():
    return sensor_readings