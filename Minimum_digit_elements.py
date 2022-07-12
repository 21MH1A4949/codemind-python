n=int(input())
x=list(map(int,input().split()))
c=0
b=len(str(min(x)))

for _ in x:
    if len(str(_))==b:
        c+=1
print(c)