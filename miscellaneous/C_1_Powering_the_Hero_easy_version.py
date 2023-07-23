import heapq

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    res = 0
    heap = []
    s = 0
    i = 0
    while i < n:
        ctr = 1
        while i < n - 1 and arr[i] == arr[i + 1] == 0:
            ctr += 1
            i += 1
        if arr[i] == 0:
            while len(heap) > ctr:
                s -= heapq.heappop(heap)
            res += s
        else:
            heapq.heappush(heap, arr[i])
            s += arr[i]
        i += 1
    print(res)