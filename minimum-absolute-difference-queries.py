from collections import defaultdict
import bisect

class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        pos = defaultdict(list)
        for i in range(n):
            pos[nums[i]].append(i)
        vals = sorted(pos)
        res = []
        for l, r in queries:
            curr = []
            for v in vals:
                if bisect.bisect_right(pos[v], r) - bisect.bisect_left(pos[v], l) > 0:
                    curr.append(v)
            if len(curr) >= 2:
                curr = min(curr[i + 1] - curr[i] for i in range(len(curr) - 1))
            else:
                curr = -1
            res.append(curr)
        return res