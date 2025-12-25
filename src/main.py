from fleet_manager import FleetManager
from electric import ElectricCar, ElectricScooter

def main():
    fleet = FleetManager()

    while True:
        print("\nFleet Management System")
        print("1. Add Hub")
        print("2. Add Vehicle to Hub")
        print("3. View All Hubs")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            hub_name = input("Enter Hub Name: ")
            fleet.add_hub(hub_name)

        elif choice == "2":
            hub_name = input("Enter Hub Name: ")

            print("\nVehicle Type:")
            print("1. Electric Car")
            print("2. Electric Scooter")
            v_type = input("Choose type: ")

            vehicle_id = input("Enter Vehicle ID: ")
            model = input("Enter Model Name: ")
            battery = int(input("Enter Battery Percentage: "))

            if v_type == "1":
                seats = int(input("Enter Seating Capacity: "))
                vehicle = ElectricCar(vehicle_id, model, battery, seats)

            elif v_type == "2":
                vehicle = ElectricScooter(vehicle_id, model, battery)

            else:
                print("Invalid vehicle type.")
                continue

            fleet.add_vehicle_to_hub(hub_name, vehicle)

        elif choice == "3":
            fleet.display_hubs()

        elif choice == "4":
            print("Exiting Fleet Management System...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
