class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        n = len(nums)
        s = sum(nums)
        res = float('inf')
        l = n * (target // s)
        target %= s
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] += p[i] + nums[i]
        for pref in range(n):
            rem = target - p[pref]
            beg = 0
            end = n - 1
            cextra = float('inf')
            while beg <= end:
                mid = (beg + end) // 2
                if p[n] - p[n - mid] == rem:
                    res = min(res, l + pref + mid)
                if p[n] - p[n - mid] >= rem:
                    end = mid - 1
                else:
                    beg = mid + 1
        last = {}
        for i in range(n + 1):
            prev = p[i] - target
            if prev in last:
                res = min(res, l + i - last[prev])
            last[p[i]] = i
        if res == float('inf'):
            return -1
        return res