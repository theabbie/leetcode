class Solution:
    def longestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        p = [0] * n
        s = [0] * n
        p[0] = arr[0]
        s[-1] = arr[-1]
        for i in range(1, n):
            if arr[i] == 1:
                p[i] = 1 + p[i - 1]
        for i in range(n - 2, -1, -1):
            if arr[i] == 1:
                s[i] = 1 + s[i + 1]
        res = 0
        if 0 in arr:
            res = max(p)
        if n >= 2:
            res = max(res, p[-2], s[1])
        for i in range(n - 2):
            res = max(res, p[i] + s[i + 2])
        return res