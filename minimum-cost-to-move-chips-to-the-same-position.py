class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        minCost = float('inf')
        for currpos in position:
            currCost = 0
            for pos in position:
                currCost += abs(pos - currpos) % 2
            minCost = min(minCost, currCost)
        return minCost