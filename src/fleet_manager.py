class FleetManager:
    def __init__(self):
        # Hub Name → List of Vehicles
        self.hubs = {}

    def add_hub(self, hub_name):
        if hub_name not in self.hubs:
            self.hubs[hub_name] = []
            print(f"Hub '{hub_name}' added.")

    def add_vehicle_to_hub(self, hub_name, vehicle):
        if hub_name in self.hubs:
            self.hubs[hub_name].append(vehicle)
            print(f"Vehicle {vehicle.vehicle_id} added to {hub_name}.")
        else:
            print("Hub does not exist.")

    # Search by Hub Location
    def search_by_hub(self, hub_name):
        if hub_name in self.hubs:
            vehicles = self.hubs[hub_name]
            if vehicles:
                print(f"\nVehicles in {hub_name} hub:")
                for v in vehicles:
                    print(f"- {v.model} ({v.vehicle_id}) | Battery: {v.battery_percentage}%")
            else:
                print("No vehicles in this hub.")
        else:
            print("Hub not found.")

    # Search by Battery > 80% using lambda & filter
    def search_by_battery(self):
        print("\nVehicles with Battery > 80%:")

        # Collect all vehicles from all hubs
        all_vehicles = []
        for vehicles in self.hubs.values():
            all_vehicles.extend(vehicles)

        #Lambda + Filter
        high_battery_vehicles = list(
            filter(lambda v: v.battery_percentage > 80, all_vehicles)
        )

        if high_battery_vehicles:
            for v in high_battery_vehicles:
                print(f"- {v.model} ({v.vehicle_id}) | Battery: {v.battery_percentage}%")
        else:
            print("No vehicles found with battery > 80%.")
