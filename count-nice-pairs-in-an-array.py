from collections import Counter

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        M = 10 ** 9 + 7
        res = 0
        ctr = Counter()
        for el in nums:
            curr = el
            rev = 0
            while el:
                rev = 10 * rev + el % 10
                el //= 10
            res += ctr[curr - rev]
            res %= M
            ctr[curr - rev] += 1
        return res