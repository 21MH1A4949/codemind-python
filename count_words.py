n=input().split()
f="aeiouAEIOU"
c=0
for i in n:
    if i[0] in f and i[-1] not in f:
        c+=1
print(c)        
