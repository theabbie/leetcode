class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        op = []
        for i in range(n):
            found = False
            for j in range(i + 1, i + n + 1):
                if nums[j % n] > nums[i]:
                    op.append(nums[j % n])
                    found = True
                    break
            if not found:
                op.append(-1)
        return op