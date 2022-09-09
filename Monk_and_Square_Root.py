for i in range(int(input())):
    n,m=map(int,input().split())
    for j in range(0,max(n,m)+1):
        if (j*j)%m==n:
            print(j)
            break
    else:
        print(-1)