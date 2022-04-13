class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        n = len(nums)
        op = []
        for i in range(n):
            op.insert(index[i], nums[i])
        return op