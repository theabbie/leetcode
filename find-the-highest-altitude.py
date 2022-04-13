class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxval = 0
        curr = 0
        for g in gain:
            curr += g
            maxval = max(maxval, curr)
        return maxval