class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [nums[(i >> 1) + n * (i & 1)] for i in range(2 * n)]