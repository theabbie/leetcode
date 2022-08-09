class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def mirrorReflection(self, p: int, q: int) -> int:
        mul = self.gcd(p, q)
        p, q = p // mul, q // mul
        return 1 - p % 2 + q % 2