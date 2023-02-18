import bisect

t = int(input())

for _ in range(t):
    n = int(input())
    q = list(map(int, input().split()))
    res = []
    unused = list(range(-n, 0))
    pos = True
    for i in range(n):
        if i == 0 or q[i] > q[i - 1]:
            res.append(q[i])
            k = bisect.bisect_left(unused, -q[i])
            unused.pop(k)
        else:
            if len(unused) == 0:
                pos = False
                break
            if -unused[-1] > q[i]:
                pos = False
                break
            res.append(-unused[-1])
            unused.pop()
    if pos:
        print(*res)
    else:
        print(-1)