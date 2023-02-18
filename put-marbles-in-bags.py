class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        parts = []
        for i in range(n - 1):
            parts.append(weights[i] + weights[i + 1])
        parts.sort()
        minval = maxval = 0
        for i in range(k - 1):
            minval += parts[i]
            maxval += parts[-(i + 1)]
        return maxval - minval