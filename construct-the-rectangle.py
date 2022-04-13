class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        i = 1
        minDiffBox = None
        while i * i <= area:
            if area % i == 0:
                if not minDiffBox or (area // i) - i < minDiffBox[0] - minDiffBox[1]:
                    minDiffBox = [area // i, i]
            i += 1
        return minDiffBox