n=int(input())
pro = 1
sum = 0
while n > 0:
    pro *= n % 10
    sum += n % 10
    n=int(n/10)
else:
    print(pro-sum)