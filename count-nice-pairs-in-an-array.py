class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        res = 0
        ctr = {}
        for el in nums:
            val = el
            rev = 0
            while el:
                rev = 10 * rev + el % 10
                el //= 10
            val -= rev
            res += ctr.get(val, 0)
            ctr[val] = ctr.get(val, 0) + 1
        return res % 1000000007