class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def lcm(self, a, b):
        return a * b // self.gcd(a, b)
    
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            lcm = 1
            for j in range(i, n):
                lcm = self.lcm(lcm, nums[j])
                if lcm == k:
                    res += 1
        return res