for i in range(int(input())):
    s=int(input())
    x=list(map(int,input().split()))
    for j in  range (s):
        if sorted(x)==x:
            print(0)
            break
        else:
            print(max(x)-min(x))
            break
        