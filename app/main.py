from app.graph.workflow import run_air_quality_workflow


def main() -> None:
    city = input("Enter an Israeli city: ")

    try:
        report = run_air_quality_workflow(city)

        print("\nAir Quality Report")
        print("------------------")
        print(f"City: {report['city']}")
        print(f"AQI: {report['aqi']}")
        print(f"Category: {report['category']}")
        print(f"Jogging safe: {report['jogging_safe']}")
        print(f"Advice: {report['advice']}")

    except ValueError as exc:
        print(f"\nError: {exc}")


if __name__ == "__main__":
    main()