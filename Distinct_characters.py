n=list(set(input().lower()))
n.sort()
for i in n:
    if i!=' ':
        print(i,end='')