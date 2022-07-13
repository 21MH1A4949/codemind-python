n=int(input())
x=list(map(int,input().split()))
a,b=(map(int,input().split()))
temp=[]
c=0
for i in range(n):
    if x[i]>=a and x[i]<=b:
        c+=1
        print(x[i],end=" ")
        
if c==0:
    print(-1)