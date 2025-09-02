M = 10 ** 9 + 7

class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        n = len(nums)
        s = [0] * (n + 1)
        ctr = [0] * (n + 1)
        ssum = Counter()
        csum = Counter()
        for j in range(n):
            ctr[j] = 1 + csum[nums[j] - 1] + csum[nums[j] + 1]
            s[j] = ssum[nums[j] - 1] + ssum[nums[j] + 1] + nums[j] * ctr[j]
            s[j] %= M
            ctr[j] %= M
            ssum[nums[j]] += s[j]
            csum[nums[j]] += ctr[j]
            ssum[nums[j]] %= M
            csum[nums[j]] %= M
        return sum(s) % M