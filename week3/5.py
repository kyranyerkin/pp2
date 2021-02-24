n=int(input())
k=int(input())
ans1=1
ans2=1
ans3=1
for i in range(1,n+1):
    ans1*=i
for i in range(1,k+1):
    ans2*=i
for i in range(1,n-k+1):
    ans3*=i
print(int(ans1/(ans2*ans3)))
