import requests


def get_city_coordinates(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }
    response = requests.get(url, params=params).json()
    if not response.get("results"):
        return None
    return {
        "lat": response["results"][0]["latitude"],
        "lon": response["results"][0]["longitude"],
        "name": response["results"][0]["name"]
    }


def fetch_weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": "true",
        "hourly": "temperature_2m,relativehumidity_2m",
        "timezone": "auto"
    }
    return requests.get(url, params=params).json()
