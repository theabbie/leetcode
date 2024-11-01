class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        M = 10 ** 9 + 7
        n = len(nums)
        s = 0
        res = 0
        ctr = Counter()
        for i in range(n):
            if ctr[nums[i]]:
                s -= pow(nums[i], ctr[nums[i]], M)
            ctr[nums[i]] += 1
            s += pow(nums[i], ctr[nums[i]], M)
            s %= M
            if i >= k:
                s -= pow(nums[i - k], ctr[nums[i - k]], M)
                ctr[nums[i - k]] -= 1
                if ctr[nums[i - k]]:
                    s += pow(nums[i - k], ctr[nums[i - k]], M)
                s %= M
            if i >= k - 1:
                res = max(res, s % M)
        return res