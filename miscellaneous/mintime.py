from collections import deque

n, h = map(int, input().split())

q = deque([(1, 1), (n, 1)])

seen = {1, n}

while len(q) > 0:
    curr, t = q.pop()
    if curr == h:
        print(t)
        break
    for nexthouse, diff in [(n - curr + 1, 0), (curr - 2, 1), (curr + 2, 1)]:
        if 1 <= nexthouse <= n and nexthouse not in seen:
            seen.add(nexthouse)
            q.appendleft((nexthouse, t + diff))