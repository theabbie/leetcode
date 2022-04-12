import heapq

class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MAX = 10 ** 9 + 7
        n = len(nums)
        heap = []
        deleted = {}
        for i, num in enumerate(nums):
            heapq.heappush(heap, (num, i))
        for _ in range(k):
            curr, j = heapq.heappop(heap)
            while (curr, j) in deleted:
                deleted[(curr, j)] -= 1
                if deleted[(curr, j)] == 0:
                    del deleted[(curr, j)]
                curr, j = heapq.heappop(heap)
            nums[j] += 1
            deleted[(curr, j)] = deleted.get((curr, j), 0) + 1
            heapq.heappush(heap, (curr + 1, j))
        p = 1
        for num in nums:
            p = (p * num) % MAX
        return p