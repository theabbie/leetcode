t = int(input())

for _ in range(t):
    s = input()
    n = len(s)
    pos = [[] for _ in range(26)]
    for i in range(n):
        pos[ord(s[i]) - ord('a')].append(i + 1)
    res = []
    k = ord(s[0]) - ord('a')
    l = ord(s[-1]) - ord('a')
    rng = None
    if k <= l:
        rng = range(k, l + 1)
    else:
        rng = range(k, l - 1, -1)
    cost = 0
    prev = k
    for i in rng:
        res.extend(pos[i])
        if len(pos[i]) > 0:
            cost += abs(i - prev)
            prev = i
    print(cost, len(res))
    print(*res)