n=list(input().lower())
c=0
l =[]
for i in n:
    if(n.count(i)==1) and i!=' ':
        l.append(i)
l.sort()
for i in l:
    print(i,end='')
