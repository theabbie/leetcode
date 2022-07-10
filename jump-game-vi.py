import heapq
from collections import defaultdict

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        heap = []
        deleted = defaultdict(int)
        heapq.heappush(heap, -nums[0])
        for i in range(1, n):
            msum = heap[0]
            while msum in deleted:
                deleted[msum] -= 1
                if deleted[msum] == 0:
                    del deleted[msum]
                heapq.heappop(heap)
                msum = heap[0]
            dp[i] = nums[i] - msum
            heapq.heappush(heap, -dp[i])
            if i >= k:
                deleted[-dp[i - k]] += 1
        return dp[n - 1]