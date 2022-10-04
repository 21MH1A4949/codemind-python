n=int(input())
x=list(map(int,input().split()))
a=sorted(x)
for i in range(n):
    print(a[i],end=" ")