def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        res = nums[0]
        for el in nums:
            res = gcd(res, el)
        return res == 1