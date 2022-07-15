n=input().split()
ms=0
ns=0
for i in n:
    print(abs(ord(max(i))-ord(min(i))),end=" ")    