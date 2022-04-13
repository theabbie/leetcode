class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        val = 0
        op = []
        for num in nums:
            val = 2 * val + num
            if val % 5 == 0:
                op.append(True)
            else:
                op.append(False)
        return op