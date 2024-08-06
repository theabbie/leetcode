class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color = {}
        ctr = Counter()
        res = []
        for x, y in queries:
            if x in color:
                ctr[color[x]] -= 1
                if ctr[color[x]] == 0:
                    del ctr[color[x]]
            color[x] = y
            ctr[color[x]] += 1
            res.append(len(ctr))
        return res