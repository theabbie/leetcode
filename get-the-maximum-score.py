class Solution:
    def maxSum(self, a, b):
        M = 10 ** 9 + 7
        m, n = len(a), len(b)
        pos = [{}, {}]
        vals = set()
        for i in range(m):
            pos[0][a[i]] = i
            vals.add(a[i])
        for i in range(n):
            pos[1][b[i]] = i
            vals.add(b[i])
        adp = [[0, 0] for _ in range(m + 1)]
        bdp = [[0, 0] for _ in range(n + 1)]
        vals = sorted(vals, reverse = True)
        for el in vals:
            if el in pos[0]:
                i = pos[0][el]
                adp[i][0] = el + max(adp[i + 1])
            if el in pos[1]:
                i = pos[1][el]
                bdp[i][0] = el + max(bdp[i + 1])
            if el in pos[0] and el in pos[1]:
                i = pos[0][el]
                j = pos[1][el]
                adp[i][1] = bdp[j][0]
                bdp[j][1] = adp[i][0]
        return max(max(adp[0]), max(bdp[0])) % M