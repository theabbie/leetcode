class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        starts = [(float('-inf'), -1)] * n
        ends = [(float('-inf'), -1)] * n
        s = 0
        for i in range(n):
            s += nums[i]
            if i >= k:
                s -= nums[i - k]
            if i >= k - 1:
                starts[i - k + 1] = (s, k - i - 1)
                ends[i] = (s, k - i - 1)
        for i in range(1, n):
            ends[i] = max(ends[i], ends[i - 1])
        for i in range(n - 2, -1, -1):
            starts[i] = max(starts[i], starts[i + 1])
        res = (float('-inf'), -n, -n, -n)
        s = 0
        for i in range(n):
            s += nums[i]
            if i >= k:
                s -= nums[i - k]
            if k - 1 < i < n - 1:
                currs = ends[i - k][0] + s + starts[i + 1][0]
                res = max(res, (currs, ends[i - k][1], k - i - 1, starts[i + 1][1]))
        return [-res[1], -res[2], -res[3]]