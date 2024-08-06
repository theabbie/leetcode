class Solution:
    def minOperations(self, nums: List[int]) -> int:
        flips = 0
        res = 0
        for el in nums:
            if flips & 1:
                el = 1 - el
            if el == 0:
                flips += 1
                res += 1
        return res