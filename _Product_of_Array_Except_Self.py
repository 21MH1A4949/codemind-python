n = int(input())

x = list(map(int,input().split()))
nums = []
for i in range(n):
    s=1
    for j in range(n):
        if i!=j:
            s*=x[j]
    nums.insert(i,s)
for i in nums:
    print(i,end=' ')