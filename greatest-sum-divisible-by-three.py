import bisect

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        msum = 0
        n = len(nums)
        total = sum(nums)
        if total % 3 == 0:
            return total
        nums.sort()
        paths = [(nums[i], [i]) for i in range(n)]
        i = 0
        while i < len(paths):
            currsum, curr = paths[i]
            if (total - currsum) % 3 == 0:
                return total - currsum
            for j in range(curr[-1] + 1, n):
                bisect.insort(paths, (currsum + nums[j], curr + [j]))
            i += 1
        return 0