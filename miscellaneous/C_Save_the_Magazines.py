import heapq
 
t = int(input())
 
for _ in range(t):
    n = int(input())
    s = list(map(int, input()))
    ctr = list(map(int, input().split()))
    lidctr = 0
    heap = []
    for i in range(n):
        heapq.heappush(heap, (ctr[i], i))
        isOne = s[i] == 1
        if s[i] == 1:
            lidctr += 1
        s[i] = 1
        if isOne and (i == n - 1 or s[i + 1] == 0):
            while len(heap) > lidctr:
                curr = heapq.heappop(heap)
                s[curr[1]] = 0
            while len(heap) > 0:
                curr = heapq.heappop(heap)
            j = i
            while j >= 0 and s[j] == 0:
                heapq.heappush(heap, (ctr[j], j))
                j -= 1
            lidctr = 0
        if i == n - 1:
            while len(heap) > 0:
                curr = heapq.heappop(heap)
                s[curr[1]] = 0
    res = 0
    for i in range(n):
        if s[i] == 1:
            res += ctr[i]
    print(res)