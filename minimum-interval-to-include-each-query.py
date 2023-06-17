import bisect

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
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n = len(intervals)
        q = len(queries)
        intervals.sort(key = lambda x: x[0] - x[1])
        for i in range(q):
            queries[i] = (queries[i], i)
        queries.sort()
        res = [-1] * q
        adds = [Heap() for _ in range(q + 1)]
        dels = [Heap() for _ in range(q + 1)]
        for a, b in intervals:
            i = bisect.bisect_left(queries, (a, float('-inf')))
            j = bisect.bisect_right(queries, (b, float('inf')))
            adds[i].push(b - a + 1)
            dels[j].push(b - a + 1)
        curr = Heap()
        for i in range(q):
            if len(adds[i]) > len(curr):
                curr, adds[i] = adds[i], curr
            while len(adds[i]) > 0:
                curr.push(adds[i].pop())
            if len(dels[i]) > len(curr):
                curr, dels[i] = dels[i], curr
            while len(dels[i]) > 0:
                curr.delete(dels[i].pop())
            res[queries[i][1]] = curr.min() if len(curr) > 0 else -1
        return res