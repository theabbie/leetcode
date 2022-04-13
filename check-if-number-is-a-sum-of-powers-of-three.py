class Solution:
    def check(self, n, used):
        if n == 0:
            return True
        if n in self.memo:
            return self.memo[n]
        k = 0
        while 3 ** k <= n:
            if k not in used and self.check(n - 3 ** k, used.union({k})):
                self.memo[n] = True
                return True
            k += 1
        self.memo[n] = False
        return False
    
    def checkPowersOfThree(self, n: int) -> bool:
        self.memo = {}
        return self.check(n, set())