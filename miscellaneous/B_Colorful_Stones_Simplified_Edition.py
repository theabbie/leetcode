s = input()
t = input()

i = 0
for el in t:
    if el == s[i]:
        i += 1

print(i + 1)