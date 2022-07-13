n=input().lower()
k=("a","e","i","o","u")
c=0
for i in n:
    if i in k:
        c+=1
print(c)        