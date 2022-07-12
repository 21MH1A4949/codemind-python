def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**.5)+1):
        if n%i==0:
            return False
    return True        




n=int(input())
m=list(map(int,input().split()))
k=int(input())
# print(k)
c=0
for i in m:
    if i<=k and prime(i):
        c+=1
print(c)        