n=int(input())
def f(x):
    cnt=0
    for i in range(1,x):
        if x%i==0:
            cnt+=i
    if cnt==x:
        return True
if f(n):
    print("perfect number")
else:
    print("not perfect number")