class Solution:
    def minDiff(self, diff, i, n, d):
        if d < 0:
            return float('inf')
        if i >= n:
            if d == 0:
                return 0
            return float('inf')
        key = (i, d)
        if key in self.cache:
            return self.cache[key]
        res = float('inf')
        currdiff = float('-inf')
        for j in range(i, n):
            currdiff = max(currdiff, diff[j])
            res = min(res, currdiff + self.minDiff(diff, j + 1, n, d - 1))
        self.cache[key] = res
        return res
    
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n:
            return -1
        self.cache = {}
        return self.minDiff(jobDifficulty, 0, n, d)