class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        res = []
        for a, b in queries:
            avals = set()
            bvals = set()
            ah = {}
            bh = {}
            while a:
                avals.add(a)
                ah[a] = len(avals) - 1
                a //= 2
            while b:
                bvals.add(b)
                bh[b] = len(bvals) - 1
                b //= 2
            lca = max(set.intersection(avals, bvals))
            res.append(1 + ah[lca] + bh[lca])
        return res