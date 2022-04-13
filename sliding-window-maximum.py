import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        maxes = []
        deleted = {}
        window = [-num for num in nums[:k]]
        heapq.heapify(window)
        maxes.append(-window[0])
        for i in range(0, n - k):
            heapq.heappush(window, -nums[i + k])
            deleted[-nums[i]] = deleted.get(-nums[i], 0) + 1
            curr = window[0]
            while curr in deleted:
                heapq.heappop(window)
                deleted[curr] -= 1
                if deleted[curr] == 0:
                    del deleted[curr]
                curr = window[0]
            maxes.append(-curr)
        return maxes