class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
x=Vehicle(200,26)
print(x.max_speed,x.mileage)