class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        n = len(nums)
        op = []
        for i in range(0, n, 2):
            op.extend([nums[i + 1]] * nums[i])
        return op