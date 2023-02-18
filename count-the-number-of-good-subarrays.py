from collections import Counter

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        curr = 0
        ctr = Counter()
        i = 0
        res = 0
        for j in range(n):
            curr += ctr[nums[j]]
            ctr[nums[j]] += 1
            while curr - ctr[nums[i]] + 1 >= k:
                curr -= ctr[nums[i]] - 1
                ctr[nums[i]] -= 1
                i += 1
            if curr >= k:
                res += i + 1
        return res