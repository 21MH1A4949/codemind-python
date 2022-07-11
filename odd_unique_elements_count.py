n=int(input())
r=set(list(map(int,input().split())))
temp=[]
c=0
for i in r:
    temp.append(i)
    if i%2==1:
        c+=1
print(c)        
