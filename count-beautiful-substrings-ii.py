class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        res = 0
        n = len(s)
        p = [[0, 0] for _ in range(n + 1)]
        for i in range(n):
            p[i + 1][0] = p[i][0] + int(s[i] in 'aeiou')
            p[i + 1][1] = p[i][1] + int(s[i] not in 'aeiou')
        vals = [i for i in range(1, n + 1) if (i * i) % (4 * k) == 0]
        if not vals:
            return res
        l = min(vals)
        ctr = defaultdict(Counter)
        for j in range(n + 1):
            res += ctr[p[j][0] - p[j][1]][j % l]
            ctr[p[j][0] - p[j][1]][j % l] += 1
        return res