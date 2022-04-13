class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        op = []
        for i in range(n):
            op.extend([nums[i], nums[i + n]])
        return op