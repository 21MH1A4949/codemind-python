def fib(n):
    t1=0
    t2=1
    nextterm=0
    print(t1,t2,end=" ")
    for i in range(n-2):
        nextterm=t1+t2
        t1=t2
        t2=nextterm
        print(nextterm,end=" ")
n=int(input())
fib(n)

    