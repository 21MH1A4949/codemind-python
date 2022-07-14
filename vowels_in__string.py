n=input()
k=("a","e","i","o","u","A","E","I","O","U")
c=0
temp=[]
for i in n:
    if i in k and i not in temp:
        temp.append(i)
        print(i,end=" ")
        c+=1
if c==0:
    print(-1)