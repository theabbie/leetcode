import bisect

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        pos = neg = 0
        for el in nums:
            if el >= 0:
                pos += el
            else:
                neg += el
        if goal >= pos:
            return goal - pos
        if goal <= neg:
            return neg - goal
        n = len(nums)
        k = n // 2
        x = [1] * max(k + 1, n - k + 1)
        for i in range(1, max(k + 1, n - k + 1)):
            x[i] = 2 * x[i - 1]
        sums = set()
        for mask in range(1 << k):
            s = 0
            for i in range(k):
                if mask & x[i]:
                    s += nums[i]
            sums.add(s)
        res = float('inf')
        sums = sorted(sums)
        for mask in range(1 << (n - k)):
            s = 0
            for i in range(n - k):
                if mask & x[i]:
                    s += nums[k + i]
            i = bisect.bisect_left(sums, goal - s)
            if i < len(sums):
                res = min(res, abs(s + sums[i] - goal))
            if i > 0:
                res = min(res, abs(s + sums[i - 1] - goal))
        return res