import bisect

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        minlen = n
        sums = [0]
        found = False
        for el in nums:
            sums.append(sums[-1] + el)
        for i in range(n + 1):
            j = bisect.bisect_left(sums, sums[i] + target)
            if j < n + 1 and sums[j] - sums[i] >= target:
                found = True
                minlen = min(minlen, j - i)
        return minlen if found else 0