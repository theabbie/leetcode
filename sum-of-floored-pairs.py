from collections import Counter
import bisect

class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        n = len(nums)
        ctr = Counter(nums)
        nums.sort()
        res = 0
        for el in ctr:
            mul = 1
            while el * mul <= nums[-1]:
                res += ctr[el] * (bisect.bisect_left(nums, el * (mul + 1)) - bisect.bisect_left(nums, el * mul)) * mul
                mul += 1
        return res % (10 ** 9 + 7)