class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        i = 1
        minDiffBox = 1
        while i * i <= area:
            if area % i == 0:
                minDiffBox = i
            i += 1
        return [area // minDiffBox, minDiffBox]