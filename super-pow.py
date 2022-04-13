class Solution:
    def pow(self, a, b, n):
        curr = 1
        for i in range(b):
            curr = ((curr % n) * (a % n)) % n
        return curr
    
    def superPow(self, a: int, b: List[int]) -> int:
        n = 1337
        if len(b) > 0:
            return (self.pow(a, b[-1], n) * self.pow(self.superPow(a, b[:-1]), 10, n)) % n
        return 1