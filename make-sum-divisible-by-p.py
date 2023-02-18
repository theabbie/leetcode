class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        k = sum(nums) % p
        if k == 0:
            return 0
        pf = [0] * (n + 1)
        for i in range(n):
            pf[i + 1] = (pf[i] + nums[i]) % p
        res = float('inf')
        lastpos = {}
        for i in range(n + 1):
            prev = pf[i] - k
            if prev < 0:
                prev += p
            if prev in lastpos:
                res = min(res, i - lastpos[prev])
            lastpos[pf[i]] = i
        if res > n - 1:
            return -1
        return res