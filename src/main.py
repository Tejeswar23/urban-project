from electric import ElectricCar
from electric import ElectricScooter

vehicles = [
    ElectricCar("C101", "Tesla", 80, 5),
    ElectricScooter("S201", "Ather", 90,4)
]

for v in vehicles:
    cost = v.calculate_trip_cost(10)
    print(f"{v.model} Trip Cost: ${cost}")