import pytest
import csv,json
from fleet_manager import FleetManager
from electric import ElectricScooter,ElectricCar

@pytest.fixture
def fleet():
    return FleetManager()

@pytest.fixture
def ec():
    return ElectricScooter("ES001", "Xiaomi M1", 85, "Scooter")

def test_add_hub_sucess(fleet, capsys):
    fleet.add_hub("Hyderabad")
    captured = capsys.readouterr()
    assert "Hub 'Hyderabad' added."in captured.out


def test_add_vehicle_to_existing_hub(fleet, ec, capsys):
    fleet.add_hub("Hyderabad")
    result = fleet.add_vehicle_to_hub("Hyderabad", ec)
    captured = capsys.readouterr()

    assert result is None
    assert ec in fleet.hubs["Hyderabad"]
    assert f"Vehicle {ec.vehicle_id} added to Hyderabad." in captured.out

def test_search_by_hub_with_vehicles(fleet, ec, capsys):
    fleet.add_hub("Hyderabad")
    fleet.add_vehicle_to_hub("Hyderabad", ec)
    fleet.search_by_hub("Hyderabad")
    captured = capsys.readouterr()
    assert "Vehicles in Hyderabad hub:" in captured.out
    assert ec.model in captured.out
    assert ec.vehicle_id in captured.out

def test_search_by_hub_empty_hub(fleet, capsys):
    fleet.add_hub("Hyderabad")
    fleet.search_by_hub("Hyderabad")
    captured = capsys.readouterr()
    assert "No vehicles in this hub." in captured.out

def test_search_by_hub_invalid_hub(fleet, capsys):
    fleet.search_by_hub("Delhi")
    captured = capsys.readouterr()
    assert "Hub not found." in captured.out
    
def test_search_by_battery_with_results(fleet, capsys):
    fleet.add_hub("Hyderabad")

    car1 = ElectricCar("EC001", "Tesla", 90, 5)
    car2 = ElectricCar("EC002", "Nissan", 75, 5)
    fleet.add_vehicle_to_hub("Hyderabad", car1)
    fleet.add_vehicle_to_hub("Hyderabad", car2)

    fleet.search_by_battery()
    captured = capsys.readouterr()

    assert "Vehicles with Battery > 80%" in captured.out
    assert "Tesla" in captured.out
    assert "EC001" in captured.out
    assert "Nissan" not in captured.out

def test_search_by_battery_no_results(fleet, capsys):
    fleet.add_hub("Hyderabad")

    car = ElectricCar("EC003", "BMW", 60, 5)
    fleet.add_vehicle_to_hub("Hyderabad", car)
    fleet.search_by_battery()
    captured = capsys.readouterr()

    assert "No vehicles found with battery > 80%." in captured.out
    
def test_view_by_vehicle_type(fleet, capsys):
    fleet.add_hub("Hyderabad")

    car = ElectricCar("EC001", "Tesla", 90, 5)
    scooter = ElectricScooter("ES001", "Xiaomi", 85, 25)
    fleet.add_vehicle_to_hub("Hyderabad", car)
    fleet.add_vehicle_to_hub("Hyderabad", scooter)

    fleet.view_by_vehicle_type()
    captured = capsys.readouterr()
    assert "cars:" in captured.out
    assert "scooters:" in captured.out
    assert "Tesla" in captured.out
    assert "Xiaomi" in captured.out

def test_view_by_vehicle_type_no_vehicles(fleet, capsys):
    fleet.view_by_vehicle_type()
    captured = capsys.readouterr()
    
    assert captured.out.strip() == ""


def test_fleet_analytics(fleet, capsys):
    fleet.add_hub("Hyderabad")

    car1 = ElectricCar("EC001", "Tesla", 90, 5)
    car2 = ElectricCar("EC002", "BMW", 80, 5)
    scooter = ElectricScooter("ES001", "Xiaomi", 85, 25)

    car1.vehicle_status = "Available"
    car2.vehicle_status = "On Trip"
    scooter.vehicle_status = "Available"

    fleet.add_vehicle_to_hub("Hyderabad", car1)
    fleet.add_vehicle_to_hub("Hyderabad", car2)
    fleet.add_vehicle_to_hub("Hyderabad", scooter)

    fleet.fleet_analytics()
    captured = capsys.readouterr()

    assert "Fleet Analytics Summary" in captured.out
    assert "Available" in captured.out
    assert "On Trip" in captured.out
    assert "Under Maintenance" in captured.out
    assert "Available" in captured.out and "2" in captured.out
    assert "On Trip" in captured.out and "1" in captured.out


def test_fleet_analytics_no_vehicles(fleet, capsys):
    fleet.fleet_analytics()
    captured = capsys.readouterr()

    assert "Available" in captured.out
    assert "0" in captured.out


def test_sort_vehicles_by_model(fleet, capsys):
    fleet.add_hub("Hyderabad")

    car1 = ElectricCar("EC001", "Tesla", 90, 5)
    car2 = ElectricCar("EC002", "BMW", 85, 5)
    car3 = ElectricCar("EC003", "Audi", 80, 5)

    fleet.add_vehicle_to_hub("Hyderabad", car1)
    fleet.add_vehicle_to_hub("Hyderabad", car2)
    fleet.add_vehicle_to_hub("Hyderabad", car3)

    fleet.sort_vehicles_by_model("Hyderabad")
    captured = capsys.readouterr()

    assert captured.out.index("Audi") < captured.out.index("BMW") < captured.out.index("Tesla")
    
def test_sort_vehicles_invalid_hub(fleet, capsys):
    fleet.sort_vehicles_by_model("Delhi")
    captured = capsys.readouterr()

    assert "Hub not found." in captured.out

def test_sort_vehicles_empty_hub(fleet, capsys):
    fleet.add_hub("Hyderabad")

    fleet.sort_vehicles_by_model("Hyderabad")
    captured = capsys.readouterr()

    assert "No vehicles in this hub." in captured.out
    
def test_sort_by_fare_price(fleet, capsys):
    fleet.add_hub("Hyderabad")

    car1 = ElectricCar("EC001", "Tesla", 90, 5)
    car2 = ElectricCar("EC002", "BMW", 85, 5)
    scooter = ElectricScooter("ES001", "Xiaomi", 80, 25)

    car1.rental_price = 500
    car2.rental_price = 400
    scooter.rental_price = 200

    fleet.add_vehicle_to_hub("Hyderabad", car1)
    fleet.add_vehicle_to_hub("Hyderabad", car2)
    fleet.add_vehicle_to_hub("Hyderabad", scooter)

    fleet.sort_by_fare_price()
    captured = capsys.readouterr()
    # Check descending order
    assert captured.out.index("Tesla") < captured.out.index("BMW") < captured.out.index("Xiaomi")
    
def test_sort_by_fare_price_no_vehicles(fleet, capsys):
    fleet.sort_by_fare_price()
    captured = capsys.readouterr()

    assert "No vehicles available." in captured.out
    


def test_save_to_csv(fleet, capsys, tmp_path):
    # Arrange
    fleet.add_hub("Hyderabad")

    car = ElectricCar("EC001", "Tesla", 90, 5)
    car.vehicle_type = "car"
    car.vehicle_status = "Available"
    car.rental_price = 500

    fleet.add_vehicle_to_hub("Hyderabad", car)

    file_path = tmp_path / "fleet.csv"

    # Act
    fleet.save_to_csv(file_path)

    # Assert file exists
    assert file_path.exists()

    # Read CSV content
    with open(file_path, newline="") as f:
        reader = list(csv.reader(f))

    # Header check
    assert reader[0] == [
        "hub_name",
        "vehicle_id",
        "model",
        "battery_percentage",
        "vehicle_type",
        "vehicle_status",
        "rental_price"
    ]

    # Data row check
    assert reader[1] == [
        "Hyderabad",
        "EC001",
        "Tesla",
        "90",
        "car",
        "Available",
        "500"
    ]

def test_load_from_csv_success(fleet, tmp_path):
    file_path = tmp_path / "fleet.csv"

    # Create CSV file
    with open(file_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "hub_name",
            "vehicle_id",
            "model",
            "battery_percentage",
            "vehicle_type",
            "vehicle_status",
            "rental_price"
        ])
        writer.writerow([
            "Hyderabad", "EC001", "Tesla", "90", "car", "Available", "500"
        ])

    # Act
    fleet.load_from_csv(file_path)

    # Assert
    assert "Hyderabad" in fleet.hubs
    assert len(fleet.hubs["Hyderabad"]) == 1

    vehicle = fleet.hubs["Hyderabad"][0]
    assert vehicle.vehicle_id == "EC001"
    assert vehicle.model == "Tesla"
    assert vehicle.battery_percentage == 90
    assert vehicle.vehicle_type == "car"
    assert vehicle.vehicle_status == "Available"
    assert vehicle.rental_price == 500.0
    

def test_save_to_json(fleet, capsys, tmp_path):
    # Arrange
    fleet.add_hub("Hyderabad")

    car = ElectricCar("EC001", "Tesla", 90, 5)
    car.vehicle_type = "car"
    car.vehicle_status = "Available"
    car.rental_price = 500

    fleet.add_vehicle_to_hub("Hyderabad", car)

    file_path = tmp_path / "fleet.json"

    # Act
    fleet.save_to_json(file_path)

    # Assert file exists
    assert file_path.exists()

    # Read JSON content
    with open(file_path) as f:
        data = json.load(f)

    assert "Hyderabad" in data
    assert len(data["Hyderabad"]) == 1

    vehicle = data["Hyderabad"][0]
    assert vehicle["vehicle_id"] == "EC001"
    assert vehicle["model"] == "Tesla"
    assert vehicle["battery_percentage"] == 90
    assert vehicle["vehicle_type"] == "car"
    assert vehicle["vehicle_status"] == "Available"
    assert vehicle["rental_price"] == 500

    # Optional: check print message
    captured = capsys.readouterr()
    assert "Fleet data saved to" in captured.out


def test_load_from_json_success(fleet, tmp_path, capsys):
    file_path = tmp_path / "fleet.json"

    data = {
        "Hyderabad": [
            {
                "vehicle_id": "EC001",
                "model": "Tesla",
                "battery_percentage": 90,
                "vehicle_type": "car",
                "vehicle_status": "Available",
                "rental_price": 500
            }
        ]
    }

    file_path.write_text(json.dumps(data))

    fleet.load_from_json(file_path)
    captured = capsys.readouterr()

    assert "Fleet data loaded from" in captured.out
    assert "Hyderabad" in fleet.hubs
    assert len(fleet.hubs["Hyderabad"]) == 1
    assert fleet.hubs["Hyderabad"][0].model == "Tesla"
    
def test_load_from_json_empty_file(fleet, tmp_path, capsys):
    file_path = tmp_path / "fleet.json"
    file_path.write_text("")

    fleet.load_from_json(file_path)
    captured = capsys.readouterr()

    assert "JSON file is empty" in captured.out
    assert fleet.hubs == {}

def test_load_from_json_file_not_found(fleet, capsys):
    fleet.load_from_json("missing.json")
    captured = capsys.readouterr()

    assert "No JSON file found" in captured.out








