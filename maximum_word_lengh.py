s = input().split()

maxc = 0
for i in s:
    if maxc<len(i):
        maxc = len(i)
print(maxc)