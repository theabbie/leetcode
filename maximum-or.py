class Solution:
    def maximumOr(self, arr, k):
        n = len(arr)
        x = 1 << k
        p = [0] * (n + 1)
        s = [0] * (n + 1)
        for i in range(n):
            p[i + 1] |= p[i] | arr[i]
            s[i + 1] |= s[i] | arr[n - i - 1]
        res = 0
        for i in range(n):
            res = max(res, p[i] | (arr[i] * x) | s[n - i - 1])
        return res