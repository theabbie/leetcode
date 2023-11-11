class Solution:
    def maxSubarraySumCircular(self, arr: List[int]) -> int:
        n = len(arr)
        total = sum(arr)
        res = total
        maxsumending = float('-inf')
        for el in arr:
            maxsumending = max(el, el + maxsumending)
            res = max(res, maxsumending)
        minsumending = float('inf')
        for el in arr:
            minsumending = min(el, el + minsumending)
            if minsumending != total:
                res = max(res, total - minsumending)
        return res
        