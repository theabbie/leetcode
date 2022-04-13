class NumArray:

    def __init__(self, nums: List[int]):
        currSum = 0
        self.sumTill = [currSum]
        for num in nums:
            currSum += num
            self.sumTill.append(currSum)

    def sumRange(self, left: int, right: int) -> int:
        return self.sumTill[right + 1] - self.sumTill[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)