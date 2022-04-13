class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)
    
    def findGCD(self, nums: List[int]) -> int:
        minNum = float('inf')
        maxNum = float('-inf')
        for num in nums:
            minNum = min(minNum, num)
            maxNum = max(maxNum, num)
        return self.gcd(minNum, maxNum)