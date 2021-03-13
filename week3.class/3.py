class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(ab):
    print("Hello my name is " + ab.name)

p1 = Person("John", 36)
p1.myfunc()
