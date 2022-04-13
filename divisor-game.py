class Solution:
    def DG(self, n: int) -> bool:
        if n in self.cache:
            return self.cache[n]
        for x in range(1, n):
            if n % x == 0 and not self.DG(n - x):
                self.cache[n] = True
                return True
        self.cache[n] = False
        return False
    
    def divisorGame(self, n: int) -> bool:
        self.cache = {}
        return self.DG(n)