s = input()

k = input()
for i in range(len(s)):
    if k==s[i]:
        print(True)
        print(i)
        break
else:
    print(False)