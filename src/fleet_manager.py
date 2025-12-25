from electric import ElectricCar
from electric import ElectricScooter

class FleetManager:
    def __init__(self):
        # Dictionary: Hub Name → List of Vehicles
        self.hubs = {}

    def add_hub(self, hub_name):
        if hub_name not in self.hubs:
            self.hubs[hub_name] = []
            print(f"Hub '{hub_name}' added successfully.")
        else:
            print("Hub already exists.")

    def add_vehicle_to_hub(self, hub_name, vehicle):
        if hub_name not in self.hubs:
            print("Hub does not exist.")
            return

        #  Duplicate vehicle_id check
        duplicate = [v for v in self.hubs[hub_name] if v == vehicle]

        if duplicate:
            print(f"Duplicate Vehicle ID '{vehicle.vehicle_id}' not allowed in {hub_name}.")
        else:
            self.hubs[hub_name].append(vehicle)
            print(f"Vehicle {vehicle.vehicle_id} added to {hub_name} hub.")

    def display_hubs(self):
        for hub, vehicles in self.hubs.items():
            print(f"\nHub: {hub}")
            for v in vehicles:
                print(f" - {v.model} ({v.vehicle_id})")
