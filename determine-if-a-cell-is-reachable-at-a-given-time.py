class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dist = max(abs(sx - fx), abs(sy - fy))
        return t >= dist if dist > 0 else t != 1