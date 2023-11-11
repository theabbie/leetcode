from collections import defaultdict
import bisect

class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        n = len(nums)
        p = 0
        pos = defaultdict(list)
        pos[0].append(0)
        for i in range(n):
            p += nums[i]
            pos[p].append(i + 1)
        res = 0
        if p % 2 == 0:
            res = bisect.bisect_right(pos[p // 2], n - 1) - bisect.bisect_left(pos[p // 2], 1)
        for i in range(n):
            diff = k - nums[i]
            if (p + diff) & 1:
                continue
            ltarget = (p + diff) // 2
            rtarget = ltarget - diff
            left = bisect.bisect_right(pos[ltarget], i) - bisect.bisect_left(pos[ltarget], 1)
            right = bisect.bisect_right(pos[rtarget], n - 1) - bisect.bisect_left(pos[rtarget], i + 1)
            res = max(res, left + right)
        return res