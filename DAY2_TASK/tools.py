import requests


def get_weather():
    latitude = 11.0168
    longitude = 76.9558

    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        f"&current=temperature_2m,precipitation,rain"
    )

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    current = data["current"]

    return {
        "temperature": current["temperature_2m"],
        "precipitation": current["precipitation"],
        "rain": current["rain"]
    }