s = input()

i = 0

while i < len(s) and s[i].islower():
    i += 1

print(i + 1)