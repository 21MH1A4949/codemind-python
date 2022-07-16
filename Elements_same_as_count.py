n=int(input())
x=list(map(int,input().split()))
temp=[]
for i in x:
    if (i == x.count(i) )and i not in temp:
        temp.append(i)
        print(i,end=" ")
    
if len(temp)==0:
    print(-1)