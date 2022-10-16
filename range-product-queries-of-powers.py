class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        M = 10 ** 9 + 7
        s = "{:b}".format(n)
        p = [0]
        for i in range(len(s)):
            if s[len(s) - i - 1] == "1":
                p.append(p[-1] + i)
        res = []
        for l, r in queries:
            res.append((1 << (p[r + 1] - p[l])) % M)
        return res