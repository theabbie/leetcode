t = int(input())

for tt in range(1, t + 1):
    n, q = map(int, input().split())
    laps = 0
    curr = 0
    vals = []
    for _ in range(q):
        d, c = input().split()
        d = int(d)
        if len(vals) == 0 or c != vals[-1][1]:
            vals.append([d, c])
        else:
            vals[-1][0] += d
    prev = vals[0][1]
    m = len(vals)
    for i in range(m):
        d, c = vals[i]
        k = (curr + d) // n
        curr = (curr + d) % n
        laps += k if prev == c else max(k - 1, 0)
        curr = (n - curr) % n
        if curr != 0 and k != 0:
            prev = c
    print(f"Case #{tt}: {laps}")