n=int(input())
x=list(map(int,input().split()))
a,b=map(int,input().split())
s=0
c=sum(x)
for i in x:
    if i >=a and i<=b:
        s+=i
print(c-s)
    