from itertools import permutations

class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        b = lambda x: "{:0b}".format(x)
        return max([int(b(x) + b(y) + b(z), 2) for x, y, z in permutations(nums)])