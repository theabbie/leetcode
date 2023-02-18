s = input()

res = 0

for c in s:
    res = 26 * res + ord(c) - ord('A') + 1

print(res)