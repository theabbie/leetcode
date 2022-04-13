class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        pos = [0]
        for d in differences:
            pos.append(pos[-1] + d)
        least = min(pos)
        pos = [p + lower - least for p in pos]
        return max(upper - max(pos) + 1, 0)