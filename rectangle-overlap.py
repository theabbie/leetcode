class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        cx1 = max(rec1[0], rec2[0])
        cx2 = min(rec1[2], rec2[2])
        cy1 = max(rec1[1], rec2[1])
        cy2 = min(rec1[3], rec2[3])
        return max(cx2 - cx1, 0) * max(cy2 - cy1, 0) != 0