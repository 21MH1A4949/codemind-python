n,k=map(int,input().split())
x=list(map(int,input().split()))
# print(x,k)
c=0
# for i in range(n):
#     if i<0:
#         i*=-1
# for i in range(n):
#     if len(str(x[i]))==k :
#         c+=1
# print(c)        
for i in x:
    if i<0:
        i*=-1
    if len(str(i))==k:
        c+=1
print(c)            