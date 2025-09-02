class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        a = Counter()
        b = Counter()
        c = Counter()
        d = 0
        res = []
        for i in range(n):
            a[A[i]] += 1
            b[B[i]] += 1
            for x in [A[i], B[i]]:
                d -= c[x]
                c[x] = min(a[x], b[x])
                d += c[x]
            res.append(d)
        return res