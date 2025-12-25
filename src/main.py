from vechile_system import VehicleSystem
from fleet_manager import FleetManager

fm = FleetManager()

fm.add_hub("Hyderabad")
fm.add_hub("Bangalore")

v1 = VehicleSystem("V101", "Tesla Model X", 90)
v2 = VehicleSystem("V102", "Ather Scooter", 60)
v3 = VehicleSystem("V103", "Nexon EV", 85)

fm.add_vehicle_to_hub("Hyderabad", v1)
fm.add_vehicle_to_hub("Hyderabad", v2)
fm.add_vehicle_to_hub("Bangalore", v3)

#  Search by Hub
fm.search_by_hub("Hyderabad")

#  Search by Battery Status
fm.search_by_battery()
