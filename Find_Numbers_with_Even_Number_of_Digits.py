n=int(input())
x=list(map(int,input().split()))
c=0
for i in x:
    if(len(str(i))%2==0):
        c+=1
print(c)    