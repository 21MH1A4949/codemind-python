n=int(input())
x=list(map(int,input().split()))

c=[]
e=[]
for i in x:
    if i %2==0:
        c.append(i)
    else:
        e.append(i)
for i in range(max(len(c),len(e))):
    if len(c)==0:
        print(e[0],end=" ")
        e.remove(e[0])
    elif len(e)==0:
        print(c[0],end=" ")
        c.remove(c[0])
    elif len(c)!=0 and len(e)!=0:
        print(c[0],e[0],end=" ")
        c.remove(c[0])
        e.remove(e[0])
    else:
        break
if n%2!=0:
    print(0)
    