class Person:
  def __init__(self, n, a):
    self.name = n
    self.age = a

  def myfunc(self):
    print(self.age + self.name)

p1 = Person(3,4)
p1.myfunc()