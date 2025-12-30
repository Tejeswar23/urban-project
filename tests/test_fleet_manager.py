import pytest
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




