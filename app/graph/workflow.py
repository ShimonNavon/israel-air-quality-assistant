from typing import TypedDict

from langgraph.graph import END, StateGraph

from app.services.interpreter import interpret_air_quality
from app.tools.air_quality import get_air_quality


class AirQualityState(TypedDict, total=False):
    city: str
    aqi: int
    category: str
    jogging_safe: bool
    advice: str
    latitude: float
    longitude: float
    country_code: str
    pm2_5: float
    pm10: float
    ozone: float
    nitrogen_dioxide: float
    sulphur_dioxide: float
    carbon_monoxide: float
    european_aqi: float
    us_aqi: float


def fetch_air_quality(state: AirQualityState) -> AirQualityState:
    raw_result = get_air_quality(state["city"])
    return raw_result


def build_report(state: AirQualityState) -> AirQualityState:
    report = interpret_air_quality(
        city=state["city"],
        aqi=state["aqi"],
    )
    return {
        **state,
        "city": report.city,
        "aqi": report.aqi,
        "category": report.category,
        "jogging_safe": report.jogging_safe,
        "advice": report.advice,
    }


def create_workflow():
    graph = StateGraph(AirQualityState)

    graph.add_node("fetch_air_quality", fetch_air_quality)
    graph.add_node("build_report", build_report)

    graph.set_entry_point("fetch_air_quality")
    graph.add_edge("fetch_air_quality", "build_report")
    graph.add_edge("build_report", END)

    return graph.compile()


app = create_workflow()


def run_air_quality_workflow(city: str):
    return app.invoke({"city": city})