class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        def solve(i):
            if i > n:
                return 0, 0
            lcost, lsum = solve(2 * i)
            rcost, rsum = solve(2 * i + 1)
            return lcost + rcost + abs(lsum - rsum), cost[i - 1] + max(lsum, rsum)
        return solve(1)[0]