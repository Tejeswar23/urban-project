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

