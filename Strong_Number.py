n=int(input())
temp=n
s=0
while temp:
    a=temp%10
    f=1
    for i in range(1,a+1):
        f*=i
    s+=f
    temp//=10
if s==n:
    print("The number",n,"is a strong number")
else:
    print("The number",n,"is not a strong number")