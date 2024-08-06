class Solution:
    def largestMerge(self, a: str, b: str) -> str:
        s = a + b
        n = len(s)
        LOG = n.bit_length() + 1
        dp = [[0] * n for _ in range(LOG)]
        pw = [1] * LOG
        for p in range(1, LOG):
            pw[p] = 2 * pw[p - 1]
        mpow = [(0, 1)] * (n + 1)
        l = 0
        p = 1
        for i in range(1, n + 1):
            if p * 2 <= i:
                l += 1
                p *= 2
            mpow[i] = (l, p)
        def rank(arr):
            n = len(arr)
            seq = sorted(range(n), key = lambda x: arr[x])
            r = 0
            prev = arr[seq[0]]
            for i in range(n):
                if i > 0 and arr[seq[i]] > prev:
                    r += 1
                prev = arr[seq[i]]
                arr[seq[i]] = r
        for l in range(LOG):
            for i in range(n):
                if l == 0:
                    dp[l][i] = (s[i], s[i])
                else:
                    dp[l][i] = (dp[l - 1][i], dp[l - 1][i + pw[l - 1]] if i + pw[l - 1] < n else n)
            rank(dp[l])
        m = len(a)
        n = len(b)
        res = []
        i = j = 0
        while i < m and j < n:
            if a[i] > b[j]:
                res.append(a[i])
                i += 1
            elif b[j] > a[i]:
                res.append(b[j])
                j += 1
            else:
                ll = min(m - i, n - j)
                l, p = mpow[ll]
                if (dp[l][i], dp[l][i + ll - p], m - i) >= (dp[l][m + j], dp[l][m + j + ll - p], n - j):
                    res.append(a[i])
                    i += 1
                else:
                    res.append(b[j])
                    j += 1
        res.append(a[i:] + b[j:])
        return "".join(res)