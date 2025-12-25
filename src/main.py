from fleet_manager import FleetManager
from vechile_system import VehicleSystem

def main():
    fm = FleetManager()

    # Add hubs
    fm.add_hub("Hyderabad")
    fm.add_hub("Bangalore")

    # Create vehicles with status
    v1 = VehicleSystem(
        vehicle_id="V101",
        model="Tesla Model X",
        battery_percentage=90,
        vehicle_type="Car",
        status="Available"
    )

    v2 = VehicleSystem(
        vehicle_id="V102",
        model="Ather Scooter",
        battery_percentage=60,
        vehicle_type="Scooter",
        status="On Trip"
    )

    v3 = VehicleSystem(
        vehicle_id="V103",
        model="Nexon EV",
        battery_percentage=85,
        vehicle_type="Car",
        status="Under Maintenance"
    )

    v4 = VehicleSystem(
        vehicle_id="V104",
        model="Ola Scooter",
        battery_percentage=75,
        vehicle_type="Scooter",
        status="Available"
    )

    # Add vehicles to hubs
    fm.add_vehicle_to_hub("Hyderabad", v1)
    fm.add_vehicle_to_hub("Hyderabad", v2)
    fm.add_vehicle_to_hub("Bangalore", v3)
    fm.add_vehicle_to_hub("Bangalore", v4)

    # UC-8: Search by Hub
    fm.search_by_hub("Hyderabad")

    # UC-8: Search by Battery
    fm.search_by_battery()

    # UC-9: Categorized View
    fm.view_by_vehicle_type()

    #  UC-10: Fleet Analytics
    fm.fleet_analytics()


if __name__ == "__main__":
    main()
