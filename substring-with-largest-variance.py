class Solution:
    def maxsum(self, arr):
        n = len(arr)
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] += p[i] + arr[i]
        msub = [float('-inf')] * n
        msub[0] = arr[0]
        for i in range(1, n):
            msub[i] = max(arr[i], arr[i] + msub[i - 1])
        lastone = lastneg = -1
        res = 0
        for i in range(n):
            if arr[i] == 1:
                if lastneg != -1:
                    res = max(res, msub[lastneg] + p[i + 1] - p[lastneg + 1])
                lastone = i
            if arr[i] == -1:
                if lastone != -1:
                    res = max(res, msub[lastone] + p[i + 1] - p[lastone + 1])
                lastneg = i
        return res
    
    def largestVariance(self, s: str) -> int:
        res = 0
        chars = set(s)
        for a in chars:
            for b in chars:
                mp = {a: 1, b: -1}
                res = max(res, self.maxsum([mp[c] for c in s if c in mp]))
        return res