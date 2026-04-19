from pydantic import BaseModel, Field


class AirQualityReport(BaseModel):
    """
    Structured result returned by the assistant.

    This is the contract of our application:
    every successful air-quality response should match this shape.
    """

    city: str = Field(..., description="City in Israel requested by the user")
    aqi: int = Field(..., description="Air Quality Index value")
    category: str = Field(..., description="Air quality category based on AQI")
    jogging_safe: bool = Field(..., description="Whether jogging outdoors is recommended")
    advice: str = Field(..., description="Short health guidance for the user")