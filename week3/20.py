a=int(input())
q1=dict()
q2=dict()
for i in range(a):
    b=input()
    l=b.split()
    q1[l[0]]=l[1]
    q2[l[1]] = l[0]
    l.clear()
c=input()
if c in q1:
  print(q1[c])
else:
    print(q2[c])