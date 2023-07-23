from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    res = []
    seq = deque(list(range(1, n + 1)))
    curr = 0
    for i in range(n):
        if i == 0 or (curr + seq[0]) % (i + 1) != 0:
            el = seq.popleft()
            res.append(el)
            curr += el
        elif len(seq) > 1 and (curr + seq[1]) % (i + 1) != 0:
            a = seq.popleft()
            b = seq.popleft()
            seq.appendleft(a)
            res.append(b)
            curr += b
    if len(res) == n:
        print(*res)
    else:
        print(-1)