class Solution:
    def smallest(self, pattern, curr, i, n, used):
        if i >= n:
            self.res = min(self.res, curr)
            return
        a, b = 1, 10
        if pattern[i] == "I":
            a = curr % 10 + 1
        else:
            b = curr % 10
        res = float('inf')
        for d in range(a, b):
            if d not in used:
                used.add(d)
                self.smallest(pattern, curr * 10 + d, i + 1, n, used)
                used.remove(d)
        return res
    
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        self.res = float('inf')
        for d in range(1, 10):
            self.smallest(pattern, d, 0, n, {d})
        return str(self.res)