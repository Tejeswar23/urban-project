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
        # UC-9: Categorized View (Car / Scooter)
    def view_by_vehicle_type(self):
        type_map = {}   # Vehicle Type → List of Vehicles

        # Collect vehicles from all hubs
        for vehicles in self.hubs.values():
            for v in vehicles:
                if v.vehicle_type not in type_map:
                    type_map[v.vehicle_type] = []
                type_map[v.vehicle_type].append(v)

        # Display vehicles type-wise
        for v_type, vehicles in type_map.items():
            print(f"\n{v_type}s:")
            for v in vehicles:
                print(f"- {v.model} ({v.vehicle_id}) | Battery: {v.battery_percentage}%")
    
    # UC-10: Fleet Analytics
    def fleet_analytics(self):
        status_count = {
            "Available": 0,
            "On Trip": 0,
            "Under Maintenance": 0
        }

        # Count vehicle statuses
        for vehicles in self.hubs.values():
            for v in vehicles:
                if v.vehicle_status in status_count:
                    status_count[v.vehicle_status] += 1

        # Display formatted summary
        print("\n Fleet Analytics Summary")
        print()
        for status, count in status_count.items():
            print(f"{status:<20}: {count}")
        print()
    
    # UC-11: Sort vehicles in a hub by Model name
    def sort_vehicles_by_model(self, hub_name):
        if hub_name not in self.hubs:
            print("Hub not found.")
            return

        vehicles = self.hubs[hub_name]

        if not vehicles:
            print("No vehicles in this hub.")
            return

        #  Sorting using key
        sorted_vehicles = sorted(vehicles, key=lambda v: v.model)

        print(f"\n Vehicles in {hub_name} hub (Sorted by Model):")
        # uses __str__
        for v in sorted_vehicles:
            print(v)  
             
