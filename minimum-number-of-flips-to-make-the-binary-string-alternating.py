class Solution:
    def minsum(self, arr, n, k):
        res = float('inf')
        curr = 0
        for i in range(n):
            curr += arr[i]
            if i >= k:
                curr -= arr[i - k]
            if i >= k - 1:
                res = min(res, curr)
        return res
    
    def minFlips(self, s: str) -> int:
        n = len(s)
        res = n
        a = [0] * n * 2
        b = [0] * n * 2
        for i in range(2 * n):
            if int(s[i % n]) != i % 2:
                a[i] = 1
            else:
                b[i] = 1
        asum = self.minsum(a, 2 * n, n)
        bsum = self.minsum(b, 2 * n, n)
        return min(asum, bsum)