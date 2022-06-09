class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        pos = {}
        res = []
        k = max(queries)
        for q in queries:
            curr = pos.get(q, q - 1)
            res.append(curr)
            for i in range(1, k + 1):
                if pos.get(i, i - 1) < curr:
                    pos[i] = pos.get(i, i - 1) + 1
            pos[q] = 0
        return res