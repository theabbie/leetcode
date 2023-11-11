class Solution:
    def maxsub(self, num, i, n, mod):
        if i >= n:
            return 0 if mod == 0 else float('-inf')
        key = (i, mod)
        if key in self.cache:
            return self.cache[key]
        a = self.maxsub(num, i + 1, n, mod)
        b = 1 + self.maxsub(num, i + 1, n, (10 * mod + int(num[i])) % 25)
        res = max(a, b)
        self.cache[key] = res
        return res
    
    def minimumOperations(self, num: str) -> int:
        self.cache = {}
        return len(num) - self.maxsub(num, 0, len(num), 0)