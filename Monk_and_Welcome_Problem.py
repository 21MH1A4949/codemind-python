n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
for i in range(n):
    print(x[i]+y[i],end=' ')
    