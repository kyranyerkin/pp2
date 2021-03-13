x=int(input())
ans = 0
while x>0:
    ans+=x%10
    x//=10
    ans*=10
else:
   print(int(ans/10))
"""
def f(x):
    ans = 0
    while(x>0):
        ans+=(x%10)
        x/=10
        ans*=10
    else:
        return ans/10
print(f(a))
"""