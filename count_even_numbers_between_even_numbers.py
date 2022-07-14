n=int(input())
x=list(map(int,input().split()))
t=0
e=0
c=0
for i in range(n):
    if x[i]%2==0:
        t=i
        break
for i in range(n-1,0,-1):
    if x[i]%2==0:
        e=i
        break
for i in range(t+1,e):
    if x[i]%2==0:
        c+=1
print(c)        
    