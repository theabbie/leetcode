import heapq

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        ctr = {}
        for num in arr:
            ctr[num] = ctr.get(num, 0) + 1
        heap = [(-v, k) for k, v in ctr.items()]
        heapq.heapify(heap)
        i = 0
        size = 0
        while size < n / 2:
            v, k = heapq.heappop(heap)
            size -= v
            i += 1
        return i