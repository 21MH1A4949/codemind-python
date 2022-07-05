s = input().split()
minc = len(s[0])
for i in s:
    c = len(i)
    if minc>=c:
        minc = c
print(minc)