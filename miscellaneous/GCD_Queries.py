from collections import defaultdict
import heapq

t = int(input())

N = 1 + 10 ** 6

sp = [1] * N
v = [False] * N

for i in range(2, N, 2):
    sp[i] = 2

for i in range(3, N, 2):
    if not v[i]:
        sp[i] = i
        j = i
        while j * i < N:
            v[j * i] = True
            sp[j * i] = i
            j += 2

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

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    vals = defaultdict(Heap)
    all = Heap()
    for el in arr:
        all.push(el)
        curr = el
        while curr > 1:
            vals[sp[curr]].push(el)
            curr //= sp[curr]
    m = int(input())
    res = []
    queries = list(map(int, input().split()))
    for q in queries:
        curr = q
        val = float('inf')
        while curr > 1:
            if len(vals[sp[curr]]) > 0:
                val = min(val, vals[sp[curr]].min())
            curr //= sp[curr]
        if val == float('inf'):
            val = all.pop()
        else:
            all.delete(val)
        res.append(val)
        curr = val
        while curr > 1:
            vals[sp[curr]].delete(val)
            curr //= sp[curr]
    print(*res)