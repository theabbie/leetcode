class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def isGoodArray(self, nums: List[int]) -> bool:
        n = len(nums)
        curr = nums[0]
        for i in range(1, n):
            curr = self.gcd(curr, nums[i])
        return curr == 1