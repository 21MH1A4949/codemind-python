n=input()
spl="`~!@#$%^&*()-_+={}[]|\;:"',.<>/?"
c=0
for i in n:
    if i in spl:
        c+=1
print(c)        