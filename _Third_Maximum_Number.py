n = int(input())
x = list(map(int,input().split()))

ma = max(x)
mi = min(x)
mcou = 1

for i in range(ma-1,mi-1,-1):
    if i in x:
        mcou+=1
        if mcou==3:
            print(i)
            break
else:
    print(ma)