from fleet_manager import FleetManager
from vechile_system import VehicleSystem

fm = FleetManager()

fm.add_hub("Hyderabad")
fm.add_hub("Bangalore")

v1 = VehicleSystem("V101", "Tesla Model X", 90, "Car")
v2 = VehicleSystem("V102", "Ather Scooter", 60, "Scooter")
v3 = VehicleSystem("V103", "Nexon EV", 85, "Car")

fm.add_vehicle_to_hub("Hyderabad", v1)
fm.add_vehicle_to_hub("Hyderabad", v2)
fm.add_vehicle_to_hub("Bangalore", v3)

# UC-9
fm.view_by_vehicle_type()
