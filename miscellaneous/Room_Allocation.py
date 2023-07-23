import heapq

n = int(input())

ranges = []

for i in range(n):
    a, b = map(int, input().split())
    ranges.append((a, b, i))

ranges.sort(key = lambda p: (p[0], -p[1]))

k = 0

res = [0] * n

heap = []

for a, b, i in ranges:
    if len(heap) > 0 and a > heap[0][0]:
        prev, room = heapq.heappop(heap)
        heapq.heappush(heap, (b, room))
        res[i] = room
    else:
        heapq.heappush(heap, (b, len(heap) + 1))
        res[i] = len(heap)
    k = max(k, len(heap))

print(k)
print(*res)