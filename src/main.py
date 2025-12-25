from fleet_manager import FleetManager
from electric import ElectricCar
from electric import ElectricScooter

fleet = FleetManager()

while True:
    print("\n1. Add Hub")
    print("2. Add Vehicle to Hub")
    print("3. View Hubs")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        hub_name = input("Enter Hub Name: ")
        fleet.add_hub(hub_name)

    elif choice == "2":
        hub_name = input("Enter Hub Name: ")

        print("1. Electric Car")
        print("2. Electric Scooter")
        vehicle_type = input("Choose Vehicle Type: ")

        vehicle_id = input("Vehicle ID: ")
        model = input("Model: ")
        battery = int(input("Battery Percentage: "))

        if vehicle_type == "1":
            seats = int(input("Seating Capacity: "))
            vehicle = ElectricCar(vehicle_id, model, battery, seats)

        elif vehicle_type == "2":
            vehicle = ElectricScooter(vehicle_id, model, battery)

        fleet.add_vehicle_to_hub(hub_name, vehicle)

    elif choice == "3":
        fleet.display_hubs()

    elif choice == "4":
        print("Exiting system...")
        break

    else:
        print("Invalid choice")
