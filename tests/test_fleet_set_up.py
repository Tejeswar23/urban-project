import pytest
from electric import ElectricScooter
from fleet_manager import FleetManager


@pytest.fixture
def ec():
    return ElectricScooter("ES001", "Xiaomi M1", 85, 25)


def test_fleet_set_up(ec):
    fm = FleetManager()
    fm.add_hub("Hyderabad")

    result = fm.add_vehicle_to_hub("Hyderabad", ec)

    assert result is None
    assert len(fm.hubs["Hyderabad"]) == 1
