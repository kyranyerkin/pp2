a=int(input())
sum=0
for i in range(100,1000):
    while i>0:
        sum+=i%10
        i/=10
    if sum==a:
        print(i)
        sum=0
    else:
        sum=0