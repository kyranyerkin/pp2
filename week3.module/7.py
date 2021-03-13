n=int(input())
sum=1
def f(x):
    ans = 1
    for i in range(1,x+1):
        ans*=i
    return ans

for i in range(1,n+1):
    sum+=1/f(i)
print("%.5f" % sum)

