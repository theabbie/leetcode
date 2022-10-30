class Solution:
    def maxsum(self, arr):
        n = len(arr)
        res = float('-inf')
        maxyet = float('-inf')
        lastneg = float('-inf')
        prev = 0
        sumneg = 0
        for i in range(n):
            if arr[i] == -1:
                lastneg = i
                sumneg = 0
            sumneg += arr[i]
            if arr[i] > arr[i] + maxyet:
                maxyet = arr[i]
                prev = i
            else:
                maxyet += arr[i]
            if prev <= lastneg:
                 res = max(res, maxyet)
            elif lastneg >= 0:
                 res = max(res, sumneg)
        return res
    
    def largestVariance(self, s: str) -> int:
        res = 0
        chars = set(s)
        for a in chars:
            for b in chars:
                curr = [1 if c == a else -1 for c in s if c == a or c == b]
                res = max(res, self.maxsum(curr))
        return res