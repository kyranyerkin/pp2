s=input()
t=s.split("-")
t.sort()
str=""
for i in t:
    str+=i+"-"
print(str[0:len(str)-1])
