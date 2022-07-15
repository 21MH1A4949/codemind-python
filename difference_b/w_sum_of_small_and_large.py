n=input().split()
ms=0
ns=0
for i in n:
    ms+=ord(min(i))
    ns+=ord(max(i))
print((ns-ms))    