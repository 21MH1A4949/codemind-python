n=input().split()
r=["a","e","i","o","u"]
mc=0

for i in n[0]:
    if i in r:
        mc+=1
for i in n:
    c=0
    for j in i:
        if j in r:
            c+=1
    if mc>c :
        mc=c
print(mc)        
    