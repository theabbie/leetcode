class Solution:
    def minimumChairs(self, s: str) -> int:
        x = 0
        res = 0
        for c in s:
            x += 1 if c == 'E' else -1
            res = max(res, x)
        return res