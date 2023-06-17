class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        n = len(s)
        pos = {}
        for l in range(1, 33):
            for i in range(n - l + 1):
                curr = int(s[i : i + l], 2)
                if curr not in pos:
                    pos[curr] = [i, i + l - 1]
        res = []
        for l, r in queries:
            q = l ^ r
            if q in pos:
                res.append(pos[q])
            else:
                res.append([-1, -1])
        return res