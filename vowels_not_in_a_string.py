n=input()
k=["a","e","i","o","u"]
temp=[]
for i in k:
    if i not in n:
        temp.append(i)
if len(temp)==0:
    print(0)
temp.sort()
for i in temp:
    print(i,end=' ')