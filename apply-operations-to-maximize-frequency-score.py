class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] = p[i] + nums[i]
        def count(i, j):
            l = j - i + 1
            pos = i + l // 2
            median = nums[pos]
            return (pos - i + 1) * median - (p[pos + 1] - p[i]) + (p[j + 1] - p[pos + 1]) - (j - pos) * median
        res = 0
        i = 0
        for j in range(n):
            while i < j and count(i, j) > k:
                i += 1
            if count(i, j) <= k:
                res = max(res, j - i + 1)
        return res