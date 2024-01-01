from collections import Counter
import bisect

M = 10 ** 9 + 7

class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        nums.sort()
        count = lambda x, y: bisect.bisect_right(nums, y) - bisect.bisect_left(nums, x)
        res = 0
        ctr = Counter(nums)
        for el in ctr:
            mul = 1
            while el * mul <= nums[-1]:
                res += ctr[el] * mul * count(el * mul, el * (mul + 1) - 1)
                res %= M
                mul += 1
        return res