from sortedcontainers import SortedList

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        s = SortedList([2 * el if el & 1 else el for el in nums])
        res = s[-1] - s[0]
        while s[-1] % 2 == 0:
            s.add(s.pop(-1) // 2)
            res = min(res, s[-1] - s[0])
        return res