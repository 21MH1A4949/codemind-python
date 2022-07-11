n = int(input())
x = list(map(int,input().split()))
r = []

for i in x:
    if i not in r:
        r.append(i)
        print(i,end=' ')
