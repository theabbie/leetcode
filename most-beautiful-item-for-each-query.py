class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        n = len(queries)
        items.sort()
        res = [0] * n
        items.sort()
        queries = sorted([(queries[i], i) for i in range(n)])
        i = 0
        maxbeauty = 0
        for q, j in queries:
            while i < len(items) and items[i][0] <= q:
                maxbeauty = max(maxbeauty, items[i][1])
                i += 1
            res[j] = maxbeauty
        return res