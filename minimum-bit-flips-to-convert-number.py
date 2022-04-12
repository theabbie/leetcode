class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return "{:b}".format(start ^ goal).count("1")