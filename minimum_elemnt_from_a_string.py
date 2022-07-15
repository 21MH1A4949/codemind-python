n=input().split()
a=n[-1]
b=min(a)
if b.isupper():
    if b.lower() in a:
        print(b.lower())
    else:
        print(b)
else:
    print(b)
