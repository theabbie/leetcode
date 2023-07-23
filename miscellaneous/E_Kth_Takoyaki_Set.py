from collections import deque

n, k = map(int, input().split())

prices = list(set(map(int, input().split())))

q = deque([({min(prices)}, min(prices), min(prices), 1)])

vals = []

while len(q) > 0:
    curr, maxval, s, t = q.pop()
    vals.append(s)
    if len(vals) > k:
        break
    nxt = float('inf')
    for el in prices:
        if el > maxval:
            nxt = min(nxt, el)
    if nxt != float('inf'):
        q.appendleft(((curr - {maxval}) | {nxt}, nxt, s - maxval + nxt, 2 * t))
        q.appendleft((curr | {nxt}, nxt, s + nxt, 2 * t + 1))

print(sorted(vals)[-1])