class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        arr = []
        for el in paths:
            arr.extend(el)
        n = len(arr)
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
                    dp[l][i] = (arr[i], arr[i])
                else:
                    dp[l][i] = (dp[l - 1][i], dp[l - 1][i + pw[l - 1]] if i + pw[l - 1] < n else n)
            rank(dp[l])
        res = 0
        beg = 1
        end = min([len(el) for el in paths])
        while beg <= end:
            mid = (beg + end) // 2
            maxocc = 0
            l, p = mpow[mid]
            ctr = {}
            off = 0
            for i in range(len(paths)):
                seen = set()
                for j in range(off, off + len(paths[i]) - mid + 1):
                    curr = (dp[l][j], dp[l][j + mid - p])
                    if curr not in seen:
                        ctr[curr] = ctr.get(curr, 0) + 1
                        maxocc = max(maxocc, ctr[curr])
                        seen.add(curr)
                off += len(paths[i])
            if maxocc == len(paths):
                res = mid
                beg = mid + 1
            else:
                end = mid - 1
        return res