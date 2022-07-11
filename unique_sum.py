n=int(input())
x=set(list(map(int,input().split())))
t=[]
s=0
for i in x:
    t.append(i)
    s+=i
print(s)    