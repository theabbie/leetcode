class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] ^= p[i] ^ arr[i]
        res = []
        for a, b in queries:
            res.append(p[b + 1] ^ p[a])
        return res