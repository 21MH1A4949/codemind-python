n=int(input())
x=list(map(int,input().split()))
c=0
d=0

for i in x:
    if i%2==0:
        c+=1
        
for i in x:
    if i%2==1:
        d+=1
print(c,d)        