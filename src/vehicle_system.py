class VehicleSystem:
    def __init__(self, vehicle_id, model, battery_percentage,vehicle_type,status="Available"):
        self.vehicle_id = vehicle_id
        self.model = model
        # added vechile type uc-9
        self.vehicle_type = vehicle_type 
        # added vechile status uc-10
        self.vehicle_status = status
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

    # Data Integrity (Duplicate Check)
    def __eq__(self, other):
        return isinstance(other, VehicleSystem) and self.vehicle_id == other.vehicle_id

    # Trip Cost (Concrete Method)
    def calculate_trip_cost(self, distance):
        return distance * 10
    
    #  UC-11: Clean print and override __str__ method
    def __str__(self):
        return (
            f"Model: {self.model}, "
            f"ID: {self.vehicle_id}, "
            f"Type: {self.vehicle_type}, "
            f"Battery: {self.battery_percentage}%, "
            f"Status: {self.vehicle_status}"
        )
