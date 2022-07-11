n=int(input())
r=list(map(int,input().split()))
for i in range(n):
    if r[i]%2==1 and i%2!=1:
        print(False)
        break
else:
    print(True)