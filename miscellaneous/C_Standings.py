from functools import cmp_to_key

n = int(input())

def cmp(x, y):
    a, b, tx = x
    c, d, ty = y
    if a * d < b * c:
        return 1
    if a * d == b * c:
        if tx > ty:
            return 1
    return -1

people = []

for _ in range(n):
    a, b = map(int, input().split())
    people.append((a, a + b, _ + 1))

people.sort(key = cmp_to_key(cmp))

print(*[p[2] for p in people])