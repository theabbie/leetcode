class Solution:
    def maximumBeauty(self, flowers: List[int]) -> int:
        n = len(flowers)
        res = float('-inf')
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] = p[i] + max(flowers[i], 0)
        mn = {}
        for i in range(n):
            res = max(res, 2 * flowers[i] + p[i] - mn.get(flowers[i], float('inf')))
            mn[flowers[i]] = min(mn.get(flowers[i], float('inf')), p[i + 1])
        return res