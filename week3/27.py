def f(n):
    return abs(int(n)-50)
l=list(int(input()).split())
m=list(l)
m.sort(key=f)
print(m)