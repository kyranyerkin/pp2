class Car:
    def __init__(self,type,volume,maxspeed,time,color):
        self.type=type
        self.volume=volume
        self.maxspeed=maxspeed
        self.time=time
        self.color=color
    def fu(self):
        print("Volume this car "+ self.type)
p=Car("sedan",3,300,3,"black")
p.fu()