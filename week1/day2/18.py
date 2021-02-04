v=[-4,-3,-2,-1,4,3,2]
v1=[0]
a=0
i=0
while i!=len(v):
    a1=a+v[i]
    v1.append(a1)
    a=a1
    i+=1
print(max(v1))



