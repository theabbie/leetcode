class Solution:
    def getSums(self, comb, target, p, res):
        if target < 0:
            return
        if p == len(comb):
            if target == 0:
                res.append(comb[1:])
            return
        for i in range(comb[p - 1] + 1, 10):
            comb[p] = i
            self.getSums(comb, target - i, p + 1, res)

    
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        comb = [0] * (k + 1)
        res = []
        self.getSums(comb, n, 1, res)
        return res