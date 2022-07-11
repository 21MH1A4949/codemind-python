n=int(input())
x=list(map(int,input().split()))
# print(n)
c=0
for i in range(n):
    if x[i]%2==0:
        print(x[i],end=" ")
for j in range(n):
    if x[j]%2==1:
        print(x[j],end=" ")
        