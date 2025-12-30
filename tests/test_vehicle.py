import pytest
from vehicle_system import VehicleSystem

@pytest.fixture
def vehicle():
    return VehicleSystem("GH009", "ROLEX M1", 70, "Scooter", "Available")

def test_set_battery(vehicle):
    vehicle.battery_percentage = 99
    value = vehicle.battery_percentage
    assert value == 99

def test_get_battery_percentage(vehicle):
    value = vehicle.battery_percentage
    assert value == 70

def test_maintence(vehicle):
    value = vehicle.maintenance_status
    assert value == "good"

def test_maintence_setter(vehicle):
    vehicle.maintenance_status = "Good"
    value = vehicle.maintenance_status
    assert value == "Good"
    
def test_rental_price_setter(vehicle):
    vehicle.rental_price = 2000
    value = vehicle.rental_price
    assert value == 2000

def test_rental_price(vehicle):
    value = vehicle.rental_price
    assert value == 0

