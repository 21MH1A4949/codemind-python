n=int(input())

for i in range(n):
    p=input()
    for i in p:
        if i.isdigit():
            print("Yes")
            break
    else:
        print("No")