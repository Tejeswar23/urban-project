from electric import ElectricCar
from fleet_manager import FleetManager
def test_car_calculate_trip_cost():
    ec = ElectricCar("EC001","Tesla x",90,5)
    cost  = ec.calculate_trip_cost(100)
    assert cost == 5.0 + (0.50 * 100)

