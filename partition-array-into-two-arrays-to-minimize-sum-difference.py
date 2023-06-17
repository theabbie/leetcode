from collections import defaultdict
import bisect

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        target = total // 2
        k = n // 2
        left = defaultdict(set)
        right = defaultdict(set)
        for mask in range(1 << k):
            l = r = 0
            ctr = 0
            for i in range(k):
                if mask & (1 << i):
                    l += nums[i]
                    r += nums[k + i]
                    ctr += 1
            left[ctr].add(l)
            right[ctr].add(r)
        for x in list(right.keys()):
            right[x] = sorted(right[x])
        res = float('inf')
        for x in left:
            for s in left[x]:
                i = bisect.bisect_left(right[k - x], target - s)
                if i < len(right[k - x]):
                    res = min(res, abs(2 * (s + right[k - x][i]) - total))
                if i > 0:
                    res = min(res, abs(2 * (s + right[k - x][i - 1]) - total))
        return res