import bisect

class SummaryRanges:

    def __init__(self):
        self.nums = []

    def addNum(self, val: int) -> None:
        n = len(self.nums)
        pos = bisect.bisect_left(self.nums, val)
        pos = min(pos, n - 1)
        if n == 0 or self.nums[pos] != val:
            bisect.insort(self.nums, val)

    def getIntervals(self) -> List[List[int]]:
        nums = self.nums
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
                ranges[i] = [ranges[i][0], ranges[i][0]]
            else:
                ranges[i] = [ranges[i][0], ranges[i][-1]]
        return ranges


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()