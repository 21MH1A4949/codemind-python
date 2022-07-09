
n=int(input())
s=0
s1=0
mat=[]
for i in range (n):
    x=list(map(int,input().split()))
    mat.append(x)
    
# print(mat)    
for i in range(n):
    for j in range(n):
    #     print(mat[i][j],end=" ")
    # print()    
            if i==j:
                s+=mat[i][j]
                
            if i==n-j-1:
                s1+=mat[i][j]
print("Principal Diagonal:"+str(s))
print("Secondary Diagonal:"+str(s1))