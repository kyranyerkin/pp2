a=int(input())
s=""
s+=str(int(a/3600)%24)+":"
a=a-int(a/3600)*3600
if int(a/60)>10:
    s+=str(int(a/60))+":"
else:
    s += "0"+str(int(a / 60)) + ":"
a=a-int(a/60)*60
if int(a%60)>10:
    s+=str(int(a%60))
else:
    s += "0"+str(int(a % 60))
print(s)
