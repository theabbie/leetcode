class Solution:
    def lca(self, a, b):
        avals = set()
        bvals = set()
        while a > 1:
            avals.add(a)
            a //= 2
        avals.add(a)
        while b > 1:
            bvals.add(b)
            b //= 2
        bvals.add(b)
        return max(set.intersection(avals, bvals))
    
    def getdepth(self, val, k):
        res = 0
        while val > k:
            res += 1
            val //= 2
        return res
    
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        res = []
        for a, b in queries:
            k = self.lca(a, b)
            if k == a:
                res.append(self.getdepth(b, 1) - self.getdepth(a, 1) + 1)
            elif k == b:
                res.append(self.getdepth(a, 1) - self.getdepth(b, 1) + 1)
            else:
                res.append(self.getdepth(a, k) + self.getdepth(b, k) + 1)
        return res