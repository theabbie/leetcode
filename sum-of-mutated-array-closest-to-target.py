class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        n = len(arr)
        total = sum(arr)
        beg = min(arr)
        end = max(arr)
        res = (float('inf'), -1)
        while beg <= end:
            mid = (beg + end) // 2
            curr = 0
            for el in arr:
                curr += el if el < mid else mid
            if curr >= target:
                res = min(res, (curr - target, mid))
                end = mid - 1
            else:
                res = min(res, (target - curr, mid))
                beg = mid + 1
        for extra in [target // n, target // n + 1]:
            curr = 0
            for el in arr:
                curr += el if el < extra else extra
            res = min(res, (abs(curr - target), extra))
        return res[1]