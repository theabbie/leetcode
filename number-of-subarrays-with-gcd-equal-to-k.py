class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            curr = nums[i]
            for j in range(i, n):
                curr = self.gcd(curr, nums[j])
                if curr == k:
                    res += 1
        return res