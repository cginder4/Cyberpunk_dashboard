import requests
import os
area = 'chicago'
os.environ["OPENWEATHER_API_KEY"] = #put your API key here (set system variable)
def get_weather(area):
    ow_api_key = os.getenv("OPENWEATHER_API_KEY")
    if not ow_api_key:
        raise ValueError("API key not found.")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={area}&units=imperial&appid={ow_api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed: {response.status_code} - {response.text}")
    data = response.json()

    temp = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    windspeed = data["wind"]["speed"]
    gust = data.get("wind", {}).get("gust", 0.0)
    precipitation = data.get("rain", {}).get("1h", 0.0)
    return {
        "temp": temp,
        "windspeed": windspeed,
        "gust": gust,
        "humidity": humidity,
        "precipitation": precipitation
    }
