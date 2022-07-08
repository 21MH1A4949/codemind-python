def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**.5)+1):
        if n%i==0:
            return False
    return True
    
n=int(input())
if prime(n):
    print(0)
else:
    after=n+1
    before=n-1
    while after:
        if prime(after):
            break
        after+=1
    while before:
        if prime(before):
            break
        before-=1
        
    diff=after-n
    diff1=n-before
    
    if diff>diff1:
        print(diff1)
        
    else:
        print(diff)