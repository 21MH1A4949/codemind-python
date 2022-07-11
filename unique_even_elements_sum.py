n=int(input())
r=set(list(map(int,input().split())))
s=0
for i in r:
    if i%2==0:
        s+=i
print(s)        