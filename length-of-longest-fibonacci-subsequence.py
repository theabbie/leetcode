class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        exists = set(arr)
        res = 0
        for j in range(n - 1, -1, -1):
            for i in range(j - 1, -1, -1):
                a = arr[i]
                b = arr[j]
                l = 2
                while b - a in exists:
                    a, b = b - a, a
                    if a >= b:
                        break
                    l += 1
                if l > 2:
                    res = max(res, l)
        return res