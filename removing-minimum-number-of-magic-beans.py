class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        n = len(beans)
        beans.sort()
        sums = [0]
        for b in beans:
            sums.append(sums[-1] + b)
        cost = sums[-1]
        for i in range(n):
            currcost = sums[-1] - sums[i] - (n - i) * beans[i] + sums[i]
            cost = min(cost, currcost)
        return cost