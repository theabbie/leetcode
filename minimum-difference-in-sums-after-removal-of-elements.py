import heapq

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        pref = [float('inf')] * (n + 1)
        suff = [float('-inf')] * (n + 1)
        prefmin = []
        prefsum = 0
        for i in range(n):
            heapq.heappush(prefmin, -nums[i])
            prefsum += nums[i]
            while 3 * len(prefmin) > n:
                prefsum += heapq.heappop(prefmin)
            if 3 * len(prefmin) == n:
                pref[i + 1] = prefsum
        suffmax = []
        suffsum = 0
        for i in range(n - 1, -1, -1):
            heapq.heappush(suffmax, nums[i])
            suffsum += nums[i]
            while 3 * len(suffmax) > n:
                suffsum -= heapq.heappop(suffmax)
            if 3 * len(suffmax) == n:
                suff[n - i] = suffsum
        res = float('inf')
        for left in range(n + 1):
            res = min(res, pref[left] - suff[n - left])
        return res