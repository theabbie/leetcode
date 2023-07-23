from collections import defaultdict
import bisect
import heapq
import math

class Heap:
    def __init__(self):
        self.heap = []
        self.deleted = defaultdict(int)

    def push(self, val):
        heapq.heappush(self.heap, val)

    def clean(self):
        while len(self.heap) > 0 and self.heap[0] in self.deleted:
            self.deleted[self.heap[0]] -= 1
            if self.deleted[self.heap[0]] == 0:
                del self.deleted[self.heap[0]]
            heapq.heappop(self.heap)

    def __len__(self):
        self.clean()
        return len(self.heap)
    
    def min(self):
        self.clean()
        return self.heap[0]
    
    def __repr__(self):
        return str(self.deleted)
    
    def delete(self, val):
        self.deleted[val] += 1

    def pop(self):
        self.clean()
        return heapq.heappop(self.heap)

n, q = map(int, input().split())

arr = list(map(int, input().split()))

queries = []

res = [-1] * q

for _ in range(q):
    l, r = map(int, input().split())
    queries.append((l - 1, r - 1))

def mos_algorithm(arr, queries):
    block_size = int(math.sqrt(len(arr)))
    sorted_queries = sorted(enumerate(queries), key=lambda x: x[1][0] // block_size)
    left, right, distinct_count = 0, -1, 0
    order = []
    heap = Heap()
    def remove(x):
        i = bisect.bisect_left(order, x)
        p = 0
        diff = 0
        for j in [i - 1, i + 1]:
            if 0 <= j < len(order):
                heap.delete(abs(order[i] - order[j]))
                p += 1
                if j == i - 1:
                    diff -= order[j]
                else:
                    diff += order[j]
        if p == 2:
            heap.push(diff)
        order.pop(i)
    def add(x):
        bisect.insort(order, x)
        i = bisect.bisect_left(order, x)
        p = 0
        diff = 0
        for j in [i - 1, i + 1]:
            if 0 <= j < len(order):
                heap.push(abs(order[i] - order[j]))
                p += 1
                if j == i - 1:
                    diff -= order[j]
                else:
                    diff += order[j]
        if p == 2:
            heap.delete(diff)
    results = [0] * len(queries)
    for query_index, (query_left, query_right) in sorted_queries:
        while left > query_left:
            left -= 1
            add(arr[left])
        while right < query_right:
            right += 1
            add(arr[right])
        while left < query_left:
            remove(arr[left])
            left += 1
        while right > query_right:
            remove(arr[right])
            right -= 1
        results[query_index] = heap.min()
    return results

print("\n".join(map(str, mos_algorithm(arr, queries))))