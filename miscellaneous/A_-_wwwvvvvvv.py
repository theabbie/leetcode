s = input()

res = 0

for c in s:
    if c == 'v':
        res += 1
    if c == 'w':
        res += 2

print(res)