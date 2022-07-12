n=int(input())
x=list(map(int,input().split()))
s=len(str(max(x)))
c=0
for i in x:
    if len(str(i))==s:
        c+=1
print(c)        