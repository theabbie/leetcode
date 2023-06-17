class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        vals = [0] * n
        for i in range(n):
            vals[i] = -(i + 1)
        res = []
        curr = 0
        for i, c in queries:
            if i > 0 and vals[i] == vals[i - 1]:
                curr -= 1
            if i < n - 1 and vals[i] == vals[i + 1]:
                curr -= 1
            vals[i] = c
            if i > 0 and vals[i] == vals[i - 1]:
                curr += 1
            if i < n - 1 and vals[i] == vals[i + 1]:
                curr += 1
            res.append(curr)
        return res