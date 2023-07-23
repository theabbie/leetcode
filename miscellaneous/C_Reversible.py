from collections import Counter

n = int(input())

seen = set()

res = 0

for _ in range(n):
    s = input()
    if s not in seen or s[::-1] not in seen:
        res += 1
    seen.add(s)
    seen.add(s[::-1])

print(res)