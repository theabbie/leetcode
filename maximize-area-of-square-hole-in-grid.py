class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        i = 0
        maxV = 1
        while i < len(vBars):
            ctr = 1
            while i < len(vBars) - 1 and vBars[i + 1] == vBars[i] + 1:
                ctr += 1
                i += 1
            maxV = max(maxV, ctr + 1)
            i += 1
        i = 0
        maxH = 1
        while i < len(hBars):
            ctr = 1
            while i < len(hBars) - 1 and hBars[i + 1] == hBars[i] + 1:
                ctr += 1
                i += 1
            maxH = max(maxH, ctr + 1)
            i += 1
        return min(maxV, maxH) * min(maxV, maxH)