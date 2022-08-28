from collections import defaultdict

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        freq = defaultdict(int)
        for l, r in requests:
            freq[l] += 1
            freq[r + 1] -= 1
        for i in range(1, n + 1):
            freq[i] += freq[i - 1]
        weights = sorted([freq[i] for i in range(n)])
        for i in range(n):
            res += nums[i] * weights[i]
        return res % (10 ** 9 + 7)