class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)
    
    def findGCD(self, nums: List[int]) -> int:
        return self.gcd(min(nums), max(nums))