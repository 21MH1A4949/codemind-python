n=int(input())
x=list(map(int,input().split()))
for i in range(n//2):
    print(x[i],x[-(i+1)],end=" ")
if n%2!=0:
    print(x[(n//2)],0)