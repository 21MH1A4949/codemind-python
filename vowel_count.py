s=input()
k=("a","e","i","o","u","A",'E','I',"O","U")
c=0
for i in s:
    if i in k:
        c+=1
print(c)        