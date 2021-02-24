a=input()
l=a.split()
cnt=0
for i in range(len(l)):
    if int(l[i])!=0:
        print(l[i])
    else:
        cnt+=1
for i in range(cnt):
    print(0)
