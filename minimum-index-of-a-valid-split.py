from collections import Counter
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
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        l = Counter()
        r = Counter(nums)
        lheap = Heap()
        rheap = Heap()
        for el in r:
            rheap.push((-r[el], el))
            lheap.push((0, el))
        for i in range(n - 1):
            lheap.delete((-l[nums[i]], nums[i]))
            l[nums[i]] += 1
            lheap.push((-l[nums[i]], nums[i]))
            rheap.delete((-r[nums[i]], nums[i]))
            r[nums[i]] -= 1
            rheap.push((-r[nums[i]], nums[i]))
            if -2 * lheap.min()[0] > i + 1 and -2 * rheap.min()[0] > n - i - 1:
                if lheap.min()[1] == rheap.min()[1]:
                    return i
        return -1