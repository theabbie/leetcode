class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if nums.count(1) > 0:
            return n - nums.count(1)
        minops = float('inf')
        for i in range(n):
            j = i
            g = nums[i]
            while j >= 0:
                g = self.gcd(g, nums[j])
                if g == 1:
                    break
                j -= 1
            if g == 1:
                minops = min(minops, i - j)
            j = i
            g = nums[i]
            while j < n:
                g = self.gcd(g, nums[j])
                if g == 1:
                    break
                j += 1
            if g == 1:
                minops = min(minops, j - i)
        if minops == float('inf'):
            return -1
        return n - 1 + minops