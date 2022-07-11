n=int(input())
x=list(map(int,input().split()))
# print(x)
# print(x)
c=0
s=sum(x)
avg=s//n
for i in range(n):
    if x[i]<=avg:
        c+=1
        # print(i)
print(c)        