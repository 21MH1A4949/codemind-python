n=(input())
# print(n)
c=1
k=["a","e","i",'o',"u"]
f=["A","E","I","O","U"]
for i in k:
    if i  not in n:
        c=0
        break


if c==0:
    for i in f:
        if i not in n:
            c=0
            break
    else:
        c=1
if c==1:
    print("True")
else :
    print(False)