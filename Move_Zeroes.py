n=int(input())
x=list(map(int,input().split()))
a=x.count(0)
for i in range(a):
    x.remove(0)
    x.append(0)
for i in x:
    print(i,end=' ')