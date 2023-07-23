from collections import defaultdict, deque
import heapq

t = int(input())

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
    
    def delete(self, val):
        self.deleted[val] += 1

    def pop(self):
        self.clean()
        return heapq.heappop(self.heap)
    
class Queue:
    def __init__(self):
        self.queue = deque()
        self.deleted = defaultdict(int)

    def push(self, val):
        self.queue.appendleft(val)

    def clean(self):
        while len(self.queue) > 0 and self.queue[-1] in self.deleted:
            self.deleted[self.queue[-1]] -= 1
            if self.deleted[self.queue[-1]] == 0:
                del self.deleted[self.queue[-1]]
            self.queue.pop()

    def __len__(self):
        self.clean()
        return len(self.queue)
    
    def delete(self, val):
        self.deleted[val] += 1

    def pop(self):
        self.clean()
        return self.queue.pop()

for _ in range(t):
    q = int(input())
    heap = Heap()
    queue = Queue()
    res = []
    id = 1
    for _ in range(q):
        curr = list(map(int, input().split()))
        if curr[0] == 1:
            heap.push((-curr[1], id))
            queue.push((curr[1], id))
            id += 1
        if curr[0] == 2:
            val, cid = queue.pop()
            heap.delete((-val, cid))
            res.append(cid)
        if curr[0] == 3:
            val, cid = heap.pop()
            val *= -1
            queue.delete((val, cid))
            res.append(cid)
    print(*res)