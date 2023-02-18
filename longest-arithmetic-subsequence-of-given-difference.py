class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        vals = {}
        for el in arr:
            if el - difference in vals:
                vals[el] = 1 + vals[el - difference]
            else:
                vals[el] = 1
        return max(vals.values())