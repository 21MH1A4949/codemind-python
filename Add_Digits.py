n=int(input())
temp=n
while True:
    s=0
    while temp:
        s+=temp%10
        temp//=10
    if len(str(s))==1:
        print(s)
        break
    else:
        temp=s