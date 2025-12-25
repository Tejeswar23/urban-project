from abc import ABC,abstractmethod
class VehicleSystem:
    def __init__(self, vehicle_id, model, battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model
        self.__battery_percentage = battery_percentage
        self.__maintenance_status = "good"
        self.__rental_price = 0

    @property
    def battery_percentage(self):
        return self.__battery_percentage

    @battery_percentage.setter
    def battery_percentage(self, value):
        if 0 < value <= 100:
            self.__battery_percentage = value
        else:
            raise ValueError("Battery percentage must be between 0 and 100")

    @property
    def maintenance_status(self):
        return self.__maintenance_status

    @maintenance_status.setter
    def maintenance_status(self, value):
        self.__maintenance_status = value

    @property
    def rental_price(self):
        return self.__rental_price

    @rental_price.setter
    def rental_price(self, value):
        if value >= 0:
            self.__rental_price = value
        else:
            raise ValueError("Rental price cannot be negative")
    
    @abstractmethod    
    def calculate_trip_cost(self,distance):
        pass