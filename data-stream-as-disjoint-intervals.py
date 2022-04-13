import bisect

class SummaryRanges:

    def __init__(self):
        self.nums = []
        self.dup = set()

    def addNum(self, val: int) -> None:
        if val not in self.dup:
            bisect.insort(self.nums, val)
            self.dup.add(val)

    def getIntervals(self) -> List[List[int]]:
        nums = self.nums
        n = len(nums)
        if n == 0:
            return []
        ranges = [[nums[0]]]
        for i in range(1, n):
            if nums[i] == ranges[-1][-1] or nums[i] == ranges[-1][-1] + 1:
                ranges[-1].append(nums[i])
            else:
                ranges.append([nums[i]])
        return [[r[0], r[-1]] for r in ranges]


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()