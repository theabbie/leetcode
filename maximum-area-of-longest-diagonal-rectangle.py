class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        res = max(dimensions, key = lambda p: (p[0] * p[0] + p[1] * p[1], p[0] * p[1]))
        return res[0] * res[1]