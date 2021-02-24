a=input()
b=input()
s=""
cnt=0
l1=a.split()
l2=b.split()
for i in range(len(l1)):
    if l1[i] in l2:
        cnt+=1
        s+=l1[i]+" "
        l2.remove(l1[i])
print(cnt)