from urllib.parse import urlencode
from urllib.request import urlopen
import json


GEOCODING_BASE_URL = "https://geocoding-api.open-meteo.com/v1/search"
AIR_QUALITY_BASE_URL = "https://air-quality-api.open-meteo.com/v1/air-quality"


def _get_json(url: str) -> dict:
    with urlopen(url, timeout=20) as response:
        return json.load(response)


def _geocode_city(city: str) -> dict:
    params = {
        "name": city,
        "count": 10,
        "language": "en",
    }
    url = f"{GEOCODING_BASE_URL}?{urlencode(params)}"
    data = _get_json(url)

    results = data.get("results") or []
    if not results:
        raise ValueError(f"Could not find city '{city}'.")

    israel_matches = [
        result for result in results
        if result.get("country_code") == "IL"
    ]

    if not israel_matches:
        raise ValueError(f"City '{city}' was found, but not in Israel.")

    return israel_matches[0]


def get_air_quality(city: str) -> dict:
    """
    Live air-quality lookup tool using Open-Meteo geocoding + air quality APIs.
    """
    location = _geocode_city(city)

    params = {
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "current": "european_aqi,us_aqi,pm2_5,pm10,ozone,nitrogen_dioxide,sulphur_dioxide,carbon_monoxide",
        "timezone": "auto",
    }
    url = f"{AIR_QUALITY_BASE_URL}?{urlencode(params)}"
    data = _get_json(url)

    current = data.get("current")
    if not current:
        raise ValueError(f"No live air-quality data returned for '{city}'.")

    aqi = current.get("us_aqi")
    if aqi is None:
        raise ValueError(f"No AQI value available for '{city}' right now.")

    return {
        "city": location["name"],
        "aqi": int(round(aqi)),
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "country_code": location["country_code"],
        "pm2_5": current.get("pm2_5"),
        "pm10": current.get("pm10"),
        "ozone": current.get("ozone"),
        "nitrogen_dioxide": current.get("nitrogen_dioxide"),
        "sulphur_dioxide": current.get("sulphur_dioxide"),
        "carbon_monoxide": current.get("carbon_monoxide"),
        "european_aqi": current.get("european_aqi"),
        "us_aqi": current.get("us_aqi"),
    }