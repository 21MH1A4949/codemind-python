n,m=map(int,input().split())
n1=list(map(int,input().split()))
m1=list(map(int,input().split()))
temp=[]
for i in n1:
    if (i in m1) and (i  not in temp):
        temp.append(i)
        print(i,end=" ")
# for i in m1:
#     if (i in n1) and (i  not in temp):
#         temp.append(i)
#     print(i,end=" ")

