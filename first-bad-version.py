# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> int:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        beg = 1
        end = n
        while beg < end:
            mid = (beg + end) // 2
            pos = isBadVersion(mid)
            if pos:
                end = mid
            else:
                beg = mid + 1
        return beg
            