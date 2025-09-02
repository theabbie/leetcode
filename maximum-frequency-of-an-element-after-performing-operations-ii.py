from collections import Counter
import bisect

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        ctr = Counter(nums)
        p = []
        for el in nums:
            p.append((el - k, 1))
            p.append((el + k + 1, -1))
        p.sort()
        res = max(ctr.values())
        r = 0
        for x, d in p:
            r += d
            res = max(res, min(r - ctr[x], numOperations) + ctr[x])
        for el in nums:
            r = bisect.bisect_right(nums, el + k) - bisect.bisect_left(nums, el - k)
            res = max(res, min(r - ctr[el], numOperations) + ctr[el])
        return res