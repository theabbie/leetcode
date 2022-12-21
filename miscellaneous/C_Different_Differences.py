t = int(input())

def numdiff(seq, n):
    d = set()
    for i in range(n - 1):
        d.add(seq[i + 1] - seq[i])
    return len(d)

for _ in range(t):
    k, n = map(int, input().split())
    res = []
    mdiff = 0
    for diff in range(n, 0, -1):
        seq = [n]
        for _ in range(k - 1):
            seq.append(seq[-1] - diff)
            diff = max(diff - 1, 1)
        seq.reverse()
        curr = numdiff(seq, k)
        if seq[0] >= 1 and curr > mdiff:
            mdiff = curr
            res = seq
    print(*res)