class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        debt = [0] * 12
        for u, v, amount in transactions:
            debt[u] -= amount
            debt[v] += amount
        debts = [d for d in debt if d != 0]
        m = len(debt)
        dp = [float('inf')] * (1 << m)
        dp[0] = 0
        for mask in range(1, 1 << m):
            s = 0
            for i in range(m):
                if mask & (1 << i):
                    s += debt[i]
            if s == 0:
                dp[mask] = mask.bit_count() - 1
                submask = mask
                while submask:
                    if s == 0:
                        dp[mask] = min(dp[mask], dp[submask] + dp[mask ^ submask])
                    submask = (submask - 1) & mask
        return dp[-1]