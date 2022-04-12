class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0:
            return []
        ranges = [[nums[0]]]
        for i in range(1, n):
            if nums[i] == ranges[-1][-1] + 1:
                ranges[-1].append(nums[i])
            else:
                ranges.append([nums[i]])
        m = len(ranges)
        for i in range(m):
            if len(ranges[i]) == 1:
                ranges[i] = "{}".format(ranges[i][0])
            else:
                ranges[i] = "{}->{}".format(ranges[i][0], ranges[i][-1])
        return ranges