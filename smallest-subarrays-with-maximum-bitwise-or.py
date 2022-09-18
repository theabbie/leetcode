import bisect

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        b = [[] for _ in range(30)]
        for i in range(n):
            for j in range(30):
                if nums[i] & (1 << j):
                    b[j].append(i)
        res = []
        for i in range(n):
            curr = 1
            for j in range(30):
                k = bisect.bisect_left(b[j], i)
                if k < len(b[j]):
                    curr = max(curr, b[j][k] - i + 1)
            res.append(curr)
        return res