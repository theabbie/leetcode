t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    last = [-1] * 32
    res = 0
    for i in range(n):
        for b in range(32):
            if arr[i] & (1 << b):
                last[b] = i
        curr = sorted(last, reverse = True)
        odd = False
        for b in range(32):
            odd = not odd
            if odd:
                res += curr[b] - curr[b - 1]
    print(res)