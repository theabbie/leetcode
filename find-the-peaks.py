class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        n = len(mountain)
        return [i for i in range(1, n - 1) if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]]