import heapq

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
        if len(self.heap) == 0:
            return float('inf')
        return self.heap[0]
    
    def __repr__(self):
        return str(self.deleted)
    
    def delete(self, val):
        self.deleted[val] += 1

    def pop(self):
        self.clean()
        return heapq.heappop(self.heap)

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        rem = Heap()
        for el in height:
            rem.push(-el)
        curr = float('-inf')
        for i in range(n):
            rem.delete(-height[i])
            h = min(curr, -rem.min())
            diff = max(h - height[i], 0)
            res += diff
            curr = max(curr, height[i])
        return res