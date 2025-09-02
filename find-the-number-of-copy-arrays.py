class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        n = len(original)
        up = min(bounds[i][1] - original[i] for i in range(n))
        down = max(bounds[i][0] - original[i] for i in range(n))
        return up - down + 1 if up >= down else 0