from electric import ElectricScooter,ElectricCar
from fleet_manager import FleetManager

def test_scooter_calculate_trip_cost():
    es = ElectricScooter("ES001","Xiaomi M1",85,25)
    cost = es.calculate_trip_cost(30)
    assert cost == 1 + (0.5 * 30)
    
def test_car_calculate_trip_cost():
    ec = ElectricCar("EC001","Tesla x",90,5)
    cost  = ec.calculate_trip_cost(100)
    assert cost == 5.0 + (0.50 * 100)