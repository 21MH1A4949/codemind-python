def rev(n):
    temp=n
    rev=0
    while temp:
        rev=rev*10+temp%10
        temp//=10
    return rev
    
    
def palin(n):
    a=rev(n)
    if a==n:
        return True
    return False    
    
x=int(input())
while True:
    x = x + rev(x)
    if palin(x):
        print(x)
        break