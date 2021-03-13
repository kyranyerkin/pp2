def f1(x):
    if x<10:
        ans="0"+str(x)
        return ans
def f(n):
    a=n//3600
    b=(n%3600)//60
    c=(n%3600)%60
    ans=f1(a) + ":" + f1(b) + ":" + f1(c)
    return ans
a=int(input())
print(f(a))

