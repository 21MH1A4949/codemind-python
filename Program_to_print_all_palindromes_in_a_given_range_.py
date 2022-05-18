a = int(input())
b = int(input())
for i in range(a,b+1):
    temp = i
    r=0
    while temp:
        r = r*10 + temp%10
        temp//=10
    if r==i:
        print(i,end=' ')