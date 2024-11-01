class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        ones = [i for i in range(len(nums)) if nums[i] == 1]
        n = len(ones)
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] = p[i] + ones[i]
        res = float('inf')
        for i in range(n - k + 1):
            median = i + k // 2
            l = median - i + 1
            lsum = p[i + l] - p[i]
            r = k - l
            rsum = p[i + l + r] - p[i + l]
            sub = l * (l - 1) // 2 + r * (r + 1) // 2
            res = min(res, ones[median] * l - lsum + rsum - ones[median] * r - sub)
        return res