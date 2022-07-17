class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        n = len(nums)
        nums.sort()
        gcd = numsDivide[0]
        for el in numsDivide:
            gcd = self.gcd(gcd, el)
        for i in range(n):
            if gcd % nums[i] == 0:
                return i
        return -1