s = input()
v = ['a','e','i','o','u']

V = ['A','E','I','O','U']
temp = []
for i  in s:
    if (i in v or i in V) and i not in temp:
        temp.append(i)
        print(i,end=' ')
if not bool(len(temp)):
    print(-1)