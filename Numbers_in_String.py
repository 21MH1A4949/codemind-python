n=list(input())
s=0
for i in n:
    if i.isdigit():
        s+=int(i)
print(s)