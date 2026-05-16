from flask import Blueprint, render_template
from services.scheduler_service import optimize_schedule
from utils.api_client import (
    fetch_depots,
    fetch_vehicles,
    fetch_logs
)

scheduler_bp = Blueprint("scheduler_bp", __name__)


# =========================
# Dashboard Route
# =========================
@scheduler_bp.route("/")
def dashboard():

    depots = fetch_depots()

    return render_template(
        "dashboard.html",
        depots=depots
    )


# =========================
# Schedule Route
# =========================
@scheduler_bp.route("/schedule")
def schedule():

    depots = fetch_depots()
    vehicles = fetch_vehicles()

    # If depot API fails
    if not depots:

        return render_template(
            "schedule.html",
            error="Unable to fetch depot data",
            result={
                "selected_vehicles": [],
                "total_hours": 0,
                "total_impact": 0
            }
        )

    # If vehicle API fails
    if not vehicles:

        return render_template(
            "schedule.html",
            error="Unable to fetch vehicle data",
            result={
                "selected_vehicles": [],
                "total_hours": 0,
                "total_impact": 0
            }
        )

    # Take first depot mechanic hours
    depot_hours = depots[0]["MechanicHours"]

    # Run optimization
    result = optimize_schedule(
        depot_hours,
        vehicles
    )

    return render_template(
        "schedule.html",
        depots=depots,
        result=result
    )


# =========================
# Vehicles Route
# =========================
@scheduler_bp.route("/vehicles")
def vehicles():

    vehicles_data = fetch_vehicles()

    return render_template(
        "vehicles.html",
        vehicles=vehicles_data
    )


# =========================
# Maintenance Route
# =========================
@scheduler_bp.route("/maintenance")
def maintenance():

    depots = fetch_depots()
    vehicles = fetch_vehicles()

    total_vehicles = len(vehicles) if vehicles else 0

    total_hours = 0

    if depots:
        for depot in depots:
            total_hours += depot["MechanicHours"]

    return render_template(
        "maintenance.html",
        depots=depots,
        total_vehicles=total_vehicles,
        total_hours=total_hours
    )


# =========================
# Logs Route
# =========================
@scheduler_bp.route("/logs")
def logs():

    logs_data = fetch_logs()

    return render_template(
        "logs.html",
        logs=logs_data
    )