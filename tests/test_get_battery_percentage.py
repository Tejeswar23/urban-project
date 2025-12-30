import pytest
from vehicle_system import VehicleSystem

@pytest.fixture
def ec():
    return VehicleSystem("ES001", "Xiaomi M1", 85, "Scooter", "Available")
def test_get_battery_percentage(ec):
    value = ec.battery_percentage
    assert value == 85