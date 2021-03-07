def f(a,b):
    l=[]
    for i in range(a,b+1):
        l.append(i*i)
    return l
a=int(input())
b=int(input())
print(f(a,b))