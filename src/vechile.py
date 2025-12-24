class Vehicle:
    def __init__(self,vehicle_id,model,battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model
        self.battery_percentage = battery_percentage
        
        
v = Vehicle("BH-321","Tesla-X",80)
print(v.vehicle_id,v.model,v.battery_percentage)
        