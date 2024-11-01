class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = 0
        mn = float('inf')
        mx = float('-inf')
        for arr in arrays:
            for el in arr:
                if mn < float('inf'):
                    res = max(res, abs(el - mn), abs(el - mx))
            for el in arr:
                mn = min(mn, el)
                mx = max(mx, el)
        return res