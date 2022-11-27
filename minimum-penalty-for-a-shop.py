class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        p = [0]
        for c in customers:
            x = 0
            if c == 'Y':
                x = 1
            p.append(p[-1] + x)
        vals = []
        for i in range(n + 1):
            curr = i + p[-1] - 2 * p[i]
            vals.append(curr)
        return vals.index(min(vals))