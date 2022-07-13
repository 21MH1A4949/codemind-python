n=int(input())
x=list(map(int,input().split()))
temp=[]
c=0
for i in x:
    if x.count(i)==1:
        temp.append(i)
        c+=1
        
if c==0:
    print(-1)
else:
    print(max(temp))