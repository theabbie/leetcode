class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        c = {}
        cc = Counter()
        res = []
        for x, y in queries:
            if x in c:
                cc[c[x]] -= 1
                if cc[c[x]] == 0:
                    del cc[c[x]]
            c[x] = y
            cc[c[x]] += 1
            res.append(len(cc))
        return res