class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        a = [0, 0]
        b = [0, 0]
        res = 0
        for c in s:
            if c == 'N':
                a[0] += 1
            if c == 'S':
                a[1] += 1
            if c == 'E':
                b[0] += 1
            if c == 'W':
                b[1] += 1
            x = min(a[0], a[1])
            y = min(b[0], b[1])
            res = max(res, abs(a[0] - a[1]) + abs(b[0] - b[1]) + 2 * min(x + y, k))
        return res