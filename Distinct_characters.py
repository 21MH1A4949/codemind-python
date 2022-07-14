s = set(input().lower())
s.discard(' ')
s = list(s)
s.sort()
for i in s:
    print(i,end='')