s1=input()
s2=input()
c=0
s1=s1.split()
s2=s2.split()
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i].lower()==s2[j].lower():
                if (s1.count(s1[i])==1 and s2.count(s2[j])==1):
                    c+=1
print(c)