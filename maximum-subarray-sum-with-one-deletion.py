class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        p = [0] * n
        s = [0] * n
        p[0] = arr[0]
        s[-1] = arr[-1]
        for i in range(1, n):
            p[i] = max(arr[i], arr[i] + p[i - 1])
        for i in range(n - 2, -1, -1):
            s[i] = max(arr[i], arr[i] + s[i + 1])
        res = max(p)
        for i in range(n - 2):
            res = max(res, p[i] + s[i + 2])
        return res