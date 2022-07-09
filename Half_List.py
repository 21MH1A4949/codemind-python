n=int(input())
n2=list(map(int,input().split()))
a=len(n2)//2
for i in range(n-1,a-1,-1):
    print(n2[i],end=" ")
for i in range(0,a):
    print(n2[i],end=" ")
    
    