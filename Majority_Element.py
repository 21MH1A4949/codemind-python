n=int(input())
x=list(map(int,input().split()))
a=n//2
for i in x:
    if x.count(i)>a:
        print(i)
        break