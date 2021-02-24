a=input()
l=a.split()
cnt=0
i=0
while cnt<len(l):
    if int(l[i])==0:
        l.pop(i)
        l.append(0)
        cnt+=1
    else:
        i+=1
for i in l:
    print(i)