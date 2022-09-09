n=int(input())
x=list(map(int,input().split()))
for i in range(len(x)):
    x[i]=x[i]**2
x.sort()

for i in x:
    print(i,end=' ')