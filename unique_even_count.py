n=int(input())
r=set(list(map(int,input().split())))
# print(r)
c=0
for i in r:
    if i%2==0:
        c+=1
print(c)        