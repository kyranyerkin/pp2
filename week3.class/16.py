l=input().split()
def f(l):
    s = {""}
    s.clear()
    s.update(l)
    if len(l) == len(s):
        return False
    else:
        return True
if f(l):
    print("Yes")
else:
    print("NO")