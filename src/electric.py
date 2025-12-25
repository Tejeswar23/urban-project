from vechile_system import VehicleSystem
class ElectricCar(VehicleSystem):
    def __init__(self, vehicle_id, model, battery_percentage, seating_capacity):
        super().__init__(vehicle_id, model, battery_percentage)
        self.seating_capacity = seating_capacity
    
        

class ElectricScooter(VehicleSystem):
    def __init__(self, vehicle_id, model, battery_percentage, max_speed_limit):
        super().__init__(vehicle_id, model, battery_percentage)
        self.max_speeed_limit = max_speed_limit
