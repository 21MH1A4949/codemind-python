n=int(input())
arr=list(map(int,input().split()))
#print(arr)
for i in range(n-1,-1,-1):
    if arr[i]%2==1:
        print(arr[i])
        break