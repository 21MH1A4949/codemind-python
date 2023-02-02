for i in range(int(input())):
    n=int(input())
    k=list(map(int,input().split()))
    h=sum(k)
    l=(n*(n+1))/2
    print(int(l-h))