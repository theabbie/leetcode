from collections import deque

t = int(input())

N = 1 + 2 * 10 ** 3

v = {0}
q = deque([(0, 0)])
res = {}

while len(q) > 0:
    curr, steps = q.pop()
    res[steps] = len(v)
    if steps >= 10 ** 6:
        continue
    if curr + 2 not in v:
        v.add(curr + 2)
        q.appendleft((curr + 2, steps + 1))
    if curr - 1 not in v:
        v.add(curr - 1)
        q.appendleft((curr - 1, steps + 1))

for _ in range(t):
    n = int(input())
    print(res[n])