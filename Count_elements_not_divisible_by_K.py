n,m=map(int,input().split())
x=list(map(int,input().split()))
c=0
for i in range(n):
    if x[i]%m!=0:
        c+=1
print(c)        
    