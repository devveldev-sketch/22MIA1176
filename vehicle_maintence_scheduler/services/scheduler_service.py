import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "http://4.224.186.213/evaluation-service"

TOKEN = os.getenv("ACCESS_TOKEN")

headers = {
    "Authorization": f"Bearer {TOKEN}"
}


def fetch_depots():

    response = requests.get(
        f"{BASE_URL}/depots",
        headers=headers
    )

    data = response.json()

    return data.get("depots", [])


def fetch_vehicles():

    response = requests.get(
        f"{BASE_URL}/vehicles",
        headers=headers
    )

    data = response.json()

    return data.get("vehicles", [])


def optimize_schedule(depot_hours, vehicles):

    vehicles = sorted(
        vehicles,
        key=lambda x: x["Impact"] / x["Duration"],
        reverse=True
    )

    selected = []
    total_hours = 0
    total_impact = 0

    for vehicle in vehicles:

        duration = vehicle["Duration"]

        if total_hours + duration <= depot_hours:
            selected.append(vehicle)
            total_hours += duration
            total_impact += vehicle["Impact"]

    return {
        "selected_vehicles": selected,
        "total_hours": total_hours,
        "total_impact": total_impact
    }