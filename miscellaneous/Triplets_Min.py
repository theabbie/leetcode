t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    freq = []
    for i in range(n):
        freq.append((n - i - 1) * (n - i - 2) // 2)
    p = [0] * (n + 1)
    for i in range(n):
        p[i + 1] += p[i] + freq[i]
    for _ in range(q):
        k = int(input())
        beg = 0
        end = n
        res = n - 1
        while beg <= end:
            mid = (beg + end) // 2
            if p[mid] >= k:
                res = arr[max(mid - 1, 0)]
                end = mid - 1
            else:
                beg = mid + 1
        print(res)