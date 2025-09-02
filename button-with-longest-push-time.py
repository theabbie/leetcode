class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        res = (-1, -1)
        prev = 0
        for pos, t in events:
            curr = t - prev
            if curr > res[0]:
                res = (curr, pos)
            if curr == res[0] and pos < res[1]:
                res = (curr, pos)
            prev = t
        return res[1]