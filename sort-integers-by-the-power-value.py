class Solution:
    def getPower(self, n):
        if n == 1:
            return 0
        if n in self.power:
            return self.power[n]
        if n & 1:
            val = 1 + self.getPower(3 * n + 1)
        else:
            val = 1 + self.getPower(n >> 1)
        self.power[n] = val
        return val
            
    
    def getKth(self, lo: int, hi: int, k: int) -> int:
        self.power = {}
        return sorted(range(lo, hi + 1), key = self.getPower)[k - 1]