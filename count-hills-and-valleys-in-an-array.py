class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n = len(nums)
        groups = []
        i = 0
        while i < n:
            ctr = 1
            while i < n - 1 and nums[i] == nums[i + 1]:
                i += 1
                ctr += 1
            i += 1
            groups.append((nums[i - 1], ctr))
        ctr = 0
        m = len(groups)
        for i in range(1, m - 1):
            left = groups[i][0] > groups[i - 1][0]
            right = groups[i][0] > groups[i + 1][0]
            if not left ^ right:
                ctr += 1
        return ctr