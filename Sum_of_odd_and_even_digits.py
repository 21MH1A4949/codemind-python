n=int(input())
x=list(map(int,input().split()))
se=0
so=0
for i in range(n):
    if i%2==0:
        so+=x[i]
    if i%2!=0:
        se+=x[i]
k=se-so
if(k==0):
    print("YES")
else:
    print("NO")
        