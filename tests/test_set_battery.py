import pytest
from vehicle_system import VehicleSystem

@pytest.fixture
def vehicle():
    return VehicleSystem("GH009", "ROLEX M1", 70, "Scooter", "Available")

def test_set_battery(vehicle):
    vehicle.battery_percentage = 99
    value = vehicle.battery_percentage
    assert value == 99
    