class Solution:
    def factors(self, n):
        i = 2
        factors = set()
        while i * i <= n:
            if n % i:
                i += 1
            else:
                while n % i == 0:
                    n //= i
                factors.add(i)
        if n > 1:
            factors.add(n)
        return factors
    
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        res = set()
        for el in nums:
            res.update(self.factors(el))
        return len(res)