from collections import Counter

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] += p[i]
            if nums[i] % modulo == k:
                p[i + 1] += 1
        print(p)
        res = 0
        ctr = Counter()
        for i in range(n + 1):
            res += ctr[(modulo + ((p[i] - k) % modulo)) % modulo]
            ctr[p[i] % modulo] += 1
        return res