import math
def fact(n):
    return (math.factorial(n))
t=int(input())
for i in range(t):
    n=int(input())
    f=fact(n)
    print(f)
    