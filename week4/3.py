q={}
l=[]
n=int(input())
for i in range(n):
    a=input()
    a1,a2=a.split(" ")
    q[a1]=a2
    l.append(a1)
l.sort()
print(l)

for i in l:
    print(q[i],i)

print("###########################################")
for x, y in q.items():
  print(x, y)