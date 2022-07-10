n=int(input())
arr=list(map(int,input().split()))
z=int(input())
c=0
for i in arr:
    if z==i:
        c+=1
print(c)        
        