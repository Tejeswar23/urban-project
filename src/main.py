from fleet_manager import FleetManager
from vechile_system import VehicleSystem

def main():
    fm = FleetManager()

    # UC-14: Load from JSON
    fm.load_from_json()

    if not fm.hubs:
        fm.add_hub("Hyderabad")
        fm.add_hub("Bangalore")

        v1 = VehicleSystem("V101", "Tesla Model X", 90, "Car", "Available")
        v1.rental_price = 3000

        v2 = VehicleSystem("V102", "Ather Scooter", 60, "Scooter", "On Trip")
        v2.rental_price = 1500

        v3 = VehicleSystem("V103", "Nexon EV", 85, "Car", "Under Maintenance")
        v3.rental_price = 2500

        fm.add_vehicle_to_hub("Hyderabad", v1)
        fm.add_vehicle_to_hub("Bangalore", v2)
        fm.add_vehicle_to_hub("Bangalore", v3)

    # Save before exit
    fm.save_to_json()

if __name__ == "__main__":
    main()
