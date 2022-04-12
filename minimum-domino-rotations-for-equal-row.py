class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        minSwaps = float('inf')
        for v in range(1, 7):
            pos = True
            currtopswaps = 0
            currbottomswaps = 0
            for i in range(n):
                if tops[i] != v and bottoms[i] != v:
                    pos = False
                    break
                else:
                    if tops[i] != v:
                        currtopswaps += 1
                    if bottoms[i] != v:
                        currbottomswaps += 1
            if pos:
                minSwaps = min(minSwaps, currtopswaps, currbottomswaps)
        return minSwaps if minSwaps != float('inf') else -1