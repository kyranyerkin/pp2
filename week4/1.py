n=int(input())
def f(x):
    if x%2==0:
        return True
    else:
        return False
for i in range(n):
    a=input()
    if not float(a):
        print("False")
    else:
        print("True")
