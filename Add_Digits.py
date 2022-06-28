n=int(input())
temp=n
while True:
    dcount=0
    s=0
    while temp:
        s+=temp%10
        dcount+=1
        temp//=10
    if dcount==1:
        print(s)
        break
    else:
        temp=s
    
    
    