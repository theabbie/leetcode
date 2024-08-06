class Solution:
    def canwin(self, rem, used, mx):
        if rem <= 0:
            return False
        key = used
        if key in self.cache:
            return self.cache[key]
        for c in range(1, mx + 1):
            if not used & (1 << c):
                if not self.canwin(rem - c, used | (1 << c), mx):
                    self.cache[key] = True
                    return True
        self.cache[key] = False
        return False
    
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal == 0:
            return True
        if maxChoosableInteger * (maxChoosableInteger + 1) < desiredTotal * 2:
            return False
        self.cache = {}
        return self.canwin(desiredTotal, 0, maxChoosableInteger)