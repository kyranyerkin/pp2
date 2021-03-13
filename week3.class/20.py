class Vihicle:
    def __init__(self,name,capacity):
        self.name=name
        self.capacity=capacity

    def fare(self):
        return self.capacity*100

class Bus(Vihicle):
    def fare(self):
        a=super().fare()
        a+=a*10/100
        return a
x=Bus("volvo",50)
print("Total Bus fare is:",x.fare())