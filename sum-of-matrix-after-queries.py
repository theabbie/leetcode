class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        q = len(queries)
        r = set()
        c = set()
        res = 0
        for i in range(q - 1, -1, -1):
            if queries[i][0] == 0 and queries[i][1] not in r:
                res += (n - len(c)) * queries[i][2]
                r.add(queries[i][1])
            if queries[i][0] == 1 and queries[i][1] not in c:
                res += (n - len(r)) * queries[i][2]
                c.add(queries[i][1])
        return res