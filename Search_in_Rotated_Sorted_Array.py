n=int(input())
x=list(map(int,input().split()))
k=int(input())
if k not in x:
    print(-1)
else:
    print(x.index(k))