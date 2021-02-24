'''
l=list(input().split())

for i in range(len(l)):
    if l[i] in l[0:i]:
        print("YES")
    else:
        print("NO")
'''
l=list(input().split())
q={}
for i in range(len(l)):
    q.update({l[i]:l.count(l[i]) })




