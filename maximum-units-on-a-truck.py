class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda b: -b[1])
        i = 0
        score = 0
        while i < len(boxTypes) and truckSize > 0:
            curr = min(boxTypes[i][0], truckSize)
            score += curr * boxTypes[i][1]
            truckSize -= curr
            i += 1
        return score