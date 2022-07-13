n=int(input())
x=list(map(int,input().split()))
temp=[]
for i in range(0,n-1,2):
    for j in range(x[i+1]):
        temp.append(x[i])
        
for i in temp:
    print(i,end=' ')