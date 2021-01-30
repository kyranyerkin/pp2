a=int(input())
b=int(input())
n=int(input())
a=a*n
a+=int((b*n)/100)
b=(b*n)%100
print(str(a)+" "+str(b))