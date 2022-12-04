s = input()
t = input()

i = 0
while i < len(s) and s[i] == t[i]:
    i += 1

print(i + 1)