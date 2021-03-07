def f(l):
    l1=[]
    for i in l:
        if int(i)%2==0:
            l1.append(i)
        else:
            continue
    return l1
print(f(input().split()))