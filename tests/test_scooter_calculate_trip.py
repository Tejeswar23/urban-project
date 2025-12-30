from electric import ElectricScooter
from fleet_manager import FleetManager

def test_scooter_calculate_trip_cost():
    es = ElectricScooter("ES001","Xiaomi M1",85,25)
    cost = es.calculate_trip_cost(30)
    assert cost == 1 + (0.5 * 30)