class Solution:
    def balancedStringSplit(self, s: str) -> int:
        vals = [0]
        for c in s:
            if c == 'L':
                vals.append(vals[-1] + 1)
            else:
                vals.append(vals[-1] - 1)
        return vals.count(0) - 1