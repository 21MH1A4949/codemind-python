n=int(input())
temp=n
r = 0 
while temp>0:
    r = r*10 + temp%10
    temp//=10
print(r==n)