class kyran:
    def __init__(self,a,b):
        self.katet1=a
        self.katet2=b
    def gipo(self):
        print(pow((pow(self.katet2,2)+pow(self.katet1,2)),1/2))
p1 = kyran(int(input()), int(input()))
p1.gipo()
