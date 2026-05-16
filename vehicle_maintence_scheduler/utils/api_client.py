import requests
from config import ACCESS_TOKEN

BASE_URL = "http://20.244.56.144/evaluation-service"


headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}


def fetch_depots():

    try:

        response = requests.get(
            f"{BASE_URL}/depots",
            headers=headers
        )

        data = response.json()

        return data.get("depots", [])

    except Exception as e:

        print("Depot API Error:", e)
        return []


def fetch_vehicles():

    # Temporary sample vehicle data

    return [

        {
            "VehicleID": "VH001",
            "MaintenanceHours": 20,
            "ImpactLevel": 50
        },

        {
            "VehicleID": "VH002",
            "MaintenanceHours": 35,
            "ImpactLevel": 80
        },

        {
            "VehicleID": "VH003",
            "MaintenanceHours": 40,
            "ImpactLevel": 100
        },

        {
            "VehicleID": "VH004",
            "MaintenanceHours": 25,
            "ImpactLevel": 60
        }

    ]


def fetch_logs():

    return [

        {
            "id": 1,
            "message": "Depot data fetched successfully"
        },

        {
            "id": 2,
            "message": "Optimization completed"
        },

        {
            "id": 3,
            "message": "Schedule generated"
        }

    ]