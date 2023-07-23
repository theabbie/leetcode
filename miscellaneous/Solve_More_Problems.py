import heapq

t = int(input())

def possible(pairs, l, k):
    n = len(pairs)
    heap = []
    total = 0
    for a, b in pairs:
        if len(heap) == l - 1 and total + a <= k:
            return True
        heapq.heappush(heap, -(a + b))
        total += a + b
        while len(heap) > l - 1:
            total += heapq.heappop(heap)
    return False

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if sum(a) + sum(b) - max(b) <= k:
        print(n)
        continue
    pairs = [(a[i], b[i]) for i in range(n)]
    pairs.sort(key = lambda x: (x[1], x[0]))
    beg = 1
    res = 0
    end = n - 1
    while beg <= end:
        mid = (beg + end) // 2
        if possible(pairs, mid, k):
            res = mid
            beg = mid + 1
        else:
            end = mid - 1
    print(res)