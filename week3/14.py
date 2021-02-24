a=input()
l=a.split()
min=1001
for i in range(len(l)):
    if int(l[i])>0 and int(l[i])<min:
        min=int(l[i])
print(min)