import random

class Solution:

    def __init__(self, nums: List[int]):
        self.valIndex = {}
        for i, num in enumerate(nums):
            self.valIndex[num] = self.valIndex.get(num, []) + [i]

    def pick(self, target: int) -> int:
        return random.choice(self.valIndex[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)