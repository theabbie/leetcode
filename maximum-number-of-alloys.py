class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        def mincost(cmp, count):
            c = 0
            for i in range(n):
                c += max(cmp[i] * count - stock[i], 0) * cost[i]
            return c
        res = 0
        for i in range(k):
            end = 1
            while mincost(composition[i], end) <= budget:
                end *= 2
            beg = end // 2
            curr = beg
            while beg <= end:
                mid = (beg + end) // 2
                if mincost(composition[i], mid) <= budget:
                    curr = mid
                    beg = mid + 1
                else:
                    end = mid - 1
            res = max(res, curr)
        return res