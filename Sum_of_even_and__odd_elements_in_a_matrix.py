n,m=map(int,input().split())
mat=[]
se=0
so=0
for i in range(n):
    x=list(map(int,input().split()))
    mat.append(x)
for i in range(n):
    for j in range(m):
        if mat[i][j]%2==0:
            se+=mat[i][j]
        else:
            so+=mat[i][j]
print(se,so)                