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
        if hub_name in self.hubs:
            self.hubs[hub_name].append(vehicle)
            print(f"Vehicle added to {hub_name} hub.")
        else:
            print("Hub does not exist.")

    def display_hubs(self):
        for hub, vehicles in self.hubs.items():
            print(f"\nHub: {hub}")
            for v in vehicles:
                print(f" - {v.model} ({v.vehicle_id})")
