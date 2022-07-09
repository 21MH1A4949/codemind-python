t=int(input())
for i in range(t):
    l,r=map(int,input().split())
    c=0
    for i in range(l,r+1):
        if str(i)[-1] in ["2",'3',"9"]:
            c+=1
    print(c)        