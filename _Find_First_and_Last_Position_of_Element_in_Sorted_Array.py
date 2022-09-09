n=int(input())
x=list(map(int,input().split()))
j=int(input())
if j not in x:
    print(-1,-1)
else:
    for i in range(n):
        if x[i]==j:
            print(i,end=" ")
            break
        
    for i in range(n-1,-1,-1):
        if x[i]==j:
            print(i,end=" ")
            break
        