class Solution:
    def maxsat(self, satisfaction, i, n, t):
        if i >= n:
            return 0
        if (i, t) in self.cache:
            return self.cache[(i, t)]
        a = self.maxsat(satisfaction, i + 1, n, t)
        b = satisfaction[i] * t + self.maxsat(satisfaction, i + 1, n, t + 1)
        res = max(a, b)
        self.cache[(i, t)] = res
        return res
    
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        satisfaction.sort()
        self.cache = {}
        return self.maxsat(satisfaction, 0, n, 1)