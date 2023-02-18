t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    minlen = float('inf')
    ctr = [0] * 101
    for _ in range(n):
        l, r = map(int, input().split())
        if l <= k <= r:
            minlen = min(minlen, r - l + 1)
            ctr[l] += 1
            ctr[r + 1] -= 1
    for i in range(1, 101):
        ctr[i] += ctr[i - 1]
    print("YES" if ctr[k] == max(ctr) and ctr.count(ctr[k]) == 1 else "NO")