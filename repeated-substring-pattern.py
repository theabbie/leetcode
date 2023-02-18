class Solution:
    def factors(self, n):
        N = n
        i = 2
        factors = set()
        while i * i <= n:
            if n % i:
                i += 1
                continue
            while n % i == 0:
                n //= i
            factors.add(i)
        if n > 1:
            factors.add(n)
        return factors
    
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for p in self.factors(n):
            l = n // p
            found = True
            for i in range(n):
                if s[i] != s[i % l]:
                    found = False
                    break
            if found:
                return True
        return False