n=int(input())
x=list(map(int,input().split()))
f=0
for i in range(2,n):
    if x[i]==x[i-2]+x[i-1]:
        f=1
    else:
        f=0
        break
if f!=1:
    print("no")
else:
    print("yes")