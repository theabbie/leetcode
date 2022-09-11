class Solution:
    def minSum(self, stones, i, n, curr, total):
        if i >= n:
            if 2 * curr < total:
                return float('inf')
            return 2 * curr - total
        key = (i, curr)
        if key in self.cache:
            return self.cache[key]
        a = self.minSum(stones, i + 1, n, curr + stones[i], total)
        b = self.minSum(stones, i + 1, n, curr, total)
        res = min(a, b)
        self.cache[key] = res
        return res
    
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        total = sum(stones)
        self.cache = {}
        return self.minSum(stones, 0, n, 0, total)