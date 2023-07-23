n = int(input())

same = True

s = input()

for i in range(0, n, 2):
    if s[i] != s[0]:
        same = False
        break

for i in range(1, n, 2):
    if s[i] != s[1]:
        same = False
        break

print("Yes" if same else "No")