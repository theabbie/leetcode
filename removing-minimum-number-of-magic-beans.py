class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        n = len(beans)
        beans.sort()
        total = sum(beans)
        cost = total
        for i in range(n):
            currcost = total - (n - i) * beans[i]
            cost = min(cost, currcost)
        return cost