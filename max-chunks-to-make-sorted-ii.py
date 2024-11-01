class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        sf = [float('inf')] * (n + 1)
        for i in range(n - 1, -1, -1):
            sf[i] = min(sf[i + 1], arr[i])
        res = 0
        i = 0
        while i < n:
            mx = float('-inf')
            while i < n and max(mx, arr[i]) > sf[i + 1]:
                mx = max(mx, arr[i])
                i += 1
            i += 1
            res += 1
        return res