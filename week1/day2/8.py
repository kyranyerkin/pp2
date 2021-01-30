a=int(input())
b=0
def f(c):
    x=int(c/60)
    y=int(c%60)
    x+=9
    print(str(x)+" "+str(y))

for i in range(1,a+1):
    if i%2==0 and i!=a:
        b+=60
    elif i%2==1 and i!=a:
        b+=50
    elif i==a:
        b+=45
f(b)