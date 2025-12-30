from vehicle_system import VehicleSystem
class ElectricCar(VehicleSystem):
    def __init__(self, vehicle_id, model, battery_percentage, seating_capacity):
        super().__init__(vehicle_id, model, battery_percentage,"car")
        self.seating_capacity = seating_capacity
    def calculate_trip_cost(self, distance):
        return 5.0 + (0.50 * distance)
   
class ElectricScooter(VehicleSystem):
    def __init__(self, vehicle_id, model, battery_percentage, max_speed_limit):
        super().__init__(vehicle_id, model, battery_percentage,"scooter")
        self.max_speed_limit = max_speed_limit
    def calculate_trip_cost(self, minutes):
        return 1 + (0.5 * minutes)