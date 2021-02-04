cnt = 0
nums=[]
n=int(input())
for i in range(n):
    a=input()
    nums.append(a)
for i in range(len(nums)):
    for j in range(len(nums)):
        if (i < j) and nums[i] == nums[j]:
            cnt += 1
print(cnt)