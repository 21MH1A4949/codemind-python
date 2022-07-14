n=input().split()
v="aeiou"
mc=0
for i in n[0]:
    if i in v:
        mc+=1
for i in n:
    c=0
    for j in i:
        if j in v:
            c+=1
    if mc>c:
        mc=c
wc=0        
for i in n:
    c=0
    for j in i:
        if j in v:
            c+=1    
    if c==mc:
        wc+=1
print(wc)        
        