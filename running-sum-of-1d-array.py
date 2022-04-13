class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        op = [0]
        for num in nums:
            op.append(op[-1] + num)
        return op[1:]