s=input()
def f(x):
    q={"bas":0,"kishi":0}
    for i in x:
        if i.isupper():
            q["bas"]+=1
        elif i.islower():
            q["kishi"]+=1
        else:
            pass
    print("bas aripter sany - ",q["bas"])
    print("kishi aripter sany - ",q["kishi"])
print(f(s))

