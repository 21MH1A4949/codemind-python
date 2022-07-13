n=int(input())
s=list(map(str,input().split()))
for i in s:
    if i[0]=='-':
        print(len(i)-1,end=' ')
    else:
        print(len(i),end=' ')