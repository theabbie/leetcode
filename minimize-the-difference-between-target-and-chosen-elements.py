import bisect

class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        m = len(mat)
        upsums = {0}
        downsums = {0}
        for i in range(m // 2):
            upsums = {x + el for el in mat[i] for x in upsums}
        for i in range(m // 2, m):
            downsums = {x + el for el in mat[i] for x in downsums}
        downsums = sorted(downsums)
        n = len(downsums)
        res = float('inf')
        for s in upsums:
            i = bisect.bisect_left(downsums, target - s)
            if i < n:
                res = min(res, abs(s + downsums[i] - target))
            if i > 0:
                res = min(res, abs(s + downsums[i - 1] - target))
        return res