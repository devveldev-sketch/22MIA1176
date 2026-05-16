from flask import Flask, render_template
import requests

app = Flask(__name__)

# =========================================
# ACCESS TOKEN
# =========================================
ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJkZXZhZGhhcnNoaW5pLnMyMDIyYkB2aXRzdHVkZW50LmFjLmluIiwiZXhwIjoxNzc4OTMyNTY1LCJpYXQiOjE3Nzg5MzE2NjUsImlzcyI6IkFmZm9yZCBNZWRpY2FsIFRlY2hub2xvZ2llcyBQcml2YXRlIExpbWl0ZWQiLCJqdGkiOiIxYzVlYzZmZC1lMDQ2LTQxOTQtODU2ZS02OTU5NzJhYjAzOWYiLCJsb2NhbGUiOiJlbi1JTiIsIm5hbWUiOiJkZXZhZGhhcnNoaW5pIHMiLCJzdWIiOiI0Y2YzYjE3My05OGFmLTQ0NGQtOGU3ZS0wZDQwYmRhZGI2ZDYifSwiZW1haWwiOiJkZXZhZGhhcnNoaW5pLnMyMDIyYkB2aXRzdHVkZW50LmFjLmluIiwibmFtZSI6ImRldmFkaGFyc2hpbmkgcyIsInJvbGxObyI6IjIybWlhMTE3NiIsImFjY2Vzc0NvZGUiOiJTZkZ1V2ciLCJjbGllbnRJRCI6IjRjZjNiMTczLTk4YWYtNDQ0ZC04ZTdlLTBkNDBiZGFkYjZkNiIsImNsaWVudFNlY3JldCI6ImV0VlNqWEZodlNoV0VDU1gifQ.voTX4HCkF29raJ4njQE7ZXAZWLOgyvZnkxKZbGEsJNg"

# =========================================
# API DETAILS
# =========================================
API_URL = "http://4.224.186.213/evaluation-service/depots"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

# =========================================
# DASHBOARD
# =========================================
@app.route("/")
@app.route("/dashboard")
def dashboard():

    response = requests.get(API_URL, headers=headers)

    depots = []

    if response.status_code == 200:

        data = response.json()

        depots = data.get("depots", [])

    return render_template(
        "dashboard.html",
        depots=depots
    )

# =========================================
# SCHEDULE PAGE
# =========================================
@app.route("/schedule")
def schedule():

    response = requests.get(API_URL, headers=headers)

    depots = []

    if response.status_code == 200:

        data = response.json()

        depots = data.get("depots", [])

    # =====================================
    # SAMPLE VEHICLE DATA
    # =====================================

    vehicles = [

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
        }

    ]

    # =====================================
    # CALCULATIONS
    # =====================================

    total_hours = sum(
        vehicle["MaintenanceHours"]
        for vehicle in vehicles
    )

    total_impact = sum(
        vehicle["ImpactLevel"]
        for vehicle in vehicles
    )

    result = {

        "selected_vehicles": vehicles,
        "total_hours": total_hours,
        "total_impact": total_impact
    }

    return render_template(

        "schedule.html",

        depots=depots,
        result=result,
        success=True
    )

# =========================================
# VEHICLES PAGE
# =========================================
@app.route("/vehicles")
def vehicles():

    vehicles_data = [

        {
            "name": "Bus A1",
            "status": "Active"
        },

        {
            "name": "Truck B2",
            "status": "Under Maintenance"
        },

        {
            "name": "Van C3",
            "status": "Available"
        },

        {
            "name": "Mini Bus D4",
            "status": "Scheduled"
        }

    ]

    return render_template(
        "vehicles.html",
        vehicles=vehicles_data
    )

# =========================================
# MAINTENANCE PAGE
# =========================================
@app.route("/maintenance")
def maintenance():

    maintenance_logs = [

        {
            "vehicle": "Bus A1",
            "date": "16 May 2026"
        },

        {
            "vehicle": "Truck B2",
            "date": "17 May 2026"
        },

        {
            "vehicle": "Van C3",
            "date": "18 May 2026"
        }

    ]

    return render_template(
        "maintenance.html",
        logs=maintenance_logs
    )

# =========================================
# LOGS PAGE
# =========================================
@app.route("/logs")
def logs():

    log_data = [

        "Depot API fetched successfully",
        "Vehicle Bus A1 scheduled",
        "Maintenance updated",
        "Optimization completed successfully"
    ]

    return render_template(
        "logs.html",
        logs=log_data
    )

# =========================================
# RUN APP
# =========================================
if __name__ == "__main__":
    app.run(debug=True)