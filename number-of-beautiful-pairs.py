class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                a = nums[i]
                while a >= 10:
                    a //= 10
                b = nums[j] % 10
                if gcd(a, b) == 1:
                    res += 1
        return res