class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        ax, ay = startPos
        bx, by = homePos
        res = 0
        for i in range(min(ay, by), max(ay + 1, by + 1)):
            res += colCosts[i]
        for i in range(min(ax, bx), max(ax + 1, bx + 1)):
            res += rowCosts[i]
        res -=  rowCosts[ax] + colCosts[ay]
        return res