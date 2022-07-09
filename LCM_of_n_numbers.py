def lcm(a,b):
    m=max(a,b)
    while True:
        if m%a==0 and m%b==0:
            return m
        m+=max(a,b)    
n=int(input())
arr=list(map(int,input().split()))
ans=lcm(arr[0],arr[1])
for i in range(1,n):
    ans=lcm(ans,arr[i])
print(ans)    