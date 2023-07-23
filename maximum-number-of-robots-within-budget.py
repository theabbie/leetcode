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
        return self.heap[0]
    
    def __repr__(self):
        return str(self.deleted)
    
    def delete(self, val):
        self.deleted[val] += 1

    def pop(self):
        self.clean()
        return heapq.heappop(self.heap)

class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        curr = Heap()
        currsum = 0
        i = 0
        res = 0
        for j in range(n):
            curr.push(-chargeTimes[j])
            currsum += runningCosts[j]
            while i < j and -curr.min() + (j - i + 1) * currsum > budget:
                currsum -= runningCosts[i]
                curr.delete(-chargeTimes[i])
                i += 1
            if -curr.min() + (j - i + 1) * currsum <= budget:
                res = max(res, j - i + 1)
        return res