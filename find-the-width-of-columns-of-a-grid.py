class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        m = 0
        for el in grid:
            m = max(m, len(el))
        res = [0] * m
        for el in grid:
            for i in range(len(el)):
                res[i] = max(res[i], len(str(el[i])))
        return res