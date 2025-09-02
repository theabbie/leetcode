class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        q = len(queries)
        beg = 0
        end = q
        res = -1
        while beg <= end:
            mid = (beg + end) // 2
            vals = [[] for _ in range(n)]
            for i in range(mid):
                l, r, v = queries[i]
                for j in range(l, r + 1):
                    vals[j].append(v)
            pos = True
            for i in range(n):
                s = {0}
                for v in vals[i]:
                    s |= {x + v for x in s}
                if nums[i] not in s:
                    pos = False
                    break
            if pos:
                res = mid
                end = mid - 1
            else:
                beg = mid + 1
        return res