a=int(input())
ans="1*"
sum=0
for i in range(a):
    sum+=i*(i+1)
for i in range(2,a):
    ans+=str(i)+"+"+str(i)+"*"
ans+=str(a)+"="+str(sum)
print(ans)