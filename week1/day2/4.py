a=int(input())
b=0
while a!=0:
    b+=a%10;
    a=a/10;
    a=int(a)

print(b)