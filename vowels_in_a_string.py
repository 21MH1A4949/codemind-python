n=input()
k=input()
for i in range(len(n)):
    if k==n[i]:
        print(True)
        print(i)
        break
else:
    print(False)