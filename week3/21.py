class Person:
  def __init__(m, name,name1, age):
    m.name = name
    m.name1 = name1
    m.age = age

  def myfunc(a):
    print("Hello my name is " + str(a.age))
    print("Hello my name is " + a.name1)

p = Person("John", "kyran",36)

p.myfunc()
