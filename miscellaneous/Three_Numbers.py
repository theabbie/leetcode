import math

t = int(input())

def solve(a, b, c):
    a, b, c = sorted([a, b, c])
    x = a + b + c
    p = math.ceil((a + c) / 2)
    if a % 2 == b % 2 == c % 2:
        return 3 * p - x
    return -1

for _ in range(t):
    a, b, c = map(int, input().split())
    print(solve(a, b, c))

from collections import deque

q = deque([(0, 0, 0, 0)])

v = {(0, 0, 0)}

while len(q) > 0:
    a, b, c, d = q.pop()
    print(d, (a, b, c))
    if d >= 10:
        break
    curr = tuple(sorted([a + 1, b + 1, c - 1]))
    if curr not in v:
        v.add(curr)
        q.appendleft((curr[0], curr[1], curr[2], d + 1))
    curr = tuple(sorted([a + 1, b - 1, c + 1]))
    if curr not in v:
        v.add(curr)
        q.appendleft((curr[0], curr[1], curr[2], d + 1))
    curr = tuple(sorted([a - 1, b + 1, c + 1]))
    if curr not in v:
        v.add(curr)
        q.appendleft((curr[0], curr[1], curr[2], d + 1))