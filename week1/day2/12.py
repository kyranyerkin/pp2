a=str(input())
def f(x):
    for i in range(len(x)):
        if x[i]!=x[len(x)-1-i]:
            return False
        else:
            return True
if f(a):
    print("Yes")
else:
    print("No")
