class Solution:
    def valid(self, s, k, n):
        for i in range(n):
            if s[i] != s[i % k]:
                return False
        return True
    
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)
        k = self.gcd(m, n)
        if self.valid(str1, k, m) and self.valid(str2, k, n) and str1[:k] == str2[:k]:
            return str1[:k]
        return ""