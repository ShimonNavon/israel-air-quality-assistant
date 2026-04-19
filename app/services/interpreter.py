from app.schemas.air_quality import AirQualityReport


def interpret_air_quality(city: str, aqi: int) -> AirQualityReport:
    """
    Convert a raw AQI value into a structured air-quality report.
    """

    if aqi <= 50:
        category = "Good"
        jogging_safe = True
        advice = "Air quality is good. Outdoor activity is safe for most people."
    elif aqi <= 100:
        category = "Moderate"
        jogging_safe = True
        advice = "Air quality is acceptable. Most people can exercise outdoors safely."
    elif aqi <= 150:
        category = "Unhealthy for Sensitive Groups"
        jogging_safe = False
        advice = "Sensitive groups should reduce outdoor exertion and avoid intense jogging."
    elif aqi <= 200:
        category = "Unhealthy"
        jogging_safe = False
        advice = "Outdoor jogging is not recommended. Limit time outside if possible."
    elif aqi <= 300:
        category = "Very Unhealthy"
        jogging_safe = False
        advice = "Avoid outdoor exercise. Stay indoors and reduce exposure."
    else:
        category = "Hazardous"
        jogging_safe = False
        advice = "Health alert conditions. Avoid going outside unless necessary."

    return AirQualityReport(
        city=city,
        aqi=aqi,
        category=category,
        jogging_safe=jogging_safe,
        advice=advice,
    )