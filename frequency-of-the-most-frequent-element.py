class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        p = [0]
        for el in nums:
            p.append(p[-1] + el)
        steps = lambda x, y: nums[y] * (y - x + 1) - p[y + 1] + p[x]
        res = 1
        i = 0
        for j in range(n):
            while i < j and steps(i, j) > k:
                i += 1
            if steps(i, j) <= k:
                res = max(res, j - i + 1)
        return res