l=[4,5,6,7,0,2,1,3]
s="codeleet"
ans=""
thisdict = {}
for i in range(len(s)):
  thisdict[l[i] ]=s[i]
for i in range(len(s)):
  ans+=thisdict[i]
print(ans)
