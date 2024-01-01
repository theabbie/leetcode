class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        M = max(nums)
        nums = set(nums)
        res = 0
        for g in range(1, M + 1):
            mul = 1
            currgcd = 0
            while g * mul <= M:
                if g * mul in nums:
                    currgcd = self.gcd(currgcd, mul)
                mul += 1
            if currgcd == 1:
                res += 1
        return res