h=int(input())
a=int(input())
b=int(input())
c=0
cnt=0
while c<h:
    c+=a
    cnt+=1
    if c>=h:
        print(cnt)
        break
    else:
        c-=b
else:
    print(cnt)