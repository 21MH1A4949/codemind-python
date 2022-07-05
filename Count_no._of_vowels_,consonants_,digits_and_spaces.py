n=list(input())
v=0
c=0
d=0
g=0

for i in n:
    if i.lower()  in ['a','e','i','o','u']:
        v+=1
        
    elif i.lower() not in ['a','e','i','o','u'] and i!=" " and not i.isdigit():
        
        c+=1
        
    elif i.lower() ==" ":
        d+=1
        
    else:
        g+=1



print("Vowels:",v)
print("Consonants:",c)
print("Digits:",g)
print("White spaces:",d)
    