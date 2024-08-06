class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        S = sum(rods) + 1
        prev = [float('-inf')] * S
        prev[0] = 0
        curr = [float('-inf')] * S
        g = lambda x: prev[x] if 0 <= x < len(prev) else float('-inf')
        for i in range(len(rods) - 1, -1, -1):
            for j in range(S):
                curr[j] = max(rods[i] + g(j + rods[i]), rods[i] + g(abs(j - rods[i])), g(j))
            prev, curr = curr, prev
        return prev[0] // 2