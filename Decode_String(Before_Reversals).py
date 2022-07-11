t=int(input())
for i  in range(t):
    n,m=map(int,input().split())
    s=input().lower()
    for i in range(m,0,-1):
        s1=s[:i]
        s1=s1[::-1]
        s2=s[i:]
        s=s1+s2
    print(s)