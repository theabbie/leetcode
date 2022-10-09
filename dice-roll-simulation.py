class Solution:
    def getcount(self, ctr, rollMax, rem):
        if rem == 0:
            return 1
        key = tuple(ctr + [rem])
        if key in self.cache:
            return self.cache[key]
        res = 0
        for i in range(6):
            if ctr[i] < rollMax[i]:
                currctr = ctr[:]
                for j in range(6):
                    currctr[j] = 0
                currctr[i] = ctr[i] + 1
                res += self.getcount(currctr, rollMax, rem - 1)
        self.cache[key] = res
        return res
    
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        ctr = [0] * 6
        self.cache = {}
        return self.getcount(ctr, rollMax, n) % (10 ** 9 + 7)