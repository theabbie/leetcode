class Solution:
    def msum(self, p, i, rem, sign):
        if rem < 0:
            return float('-inf')
        if i >= len(p):
            if rem == 0 and sign == -1:
                return 0
            return float('-inf')
        key = (i, rem, sign)
        if key in self.cache:
            return self.cache[key]
        a = self.msum(p, i + 1, rem, sign)
        x = (rem + 1) // 2
        s = 1 if x & 1 else -1
        b = sign * p[i] * x * s + self.msum(p, i + 1, rem - 1, -sign)
        c = float('-inf')
        if sign == 1:
            c = p[i] * x * s + p[i] * (x - 1) * s + self.msum(p, i + 1, rem - 2, sign)
        res = max(a, b, c)
        self.cache[key] = res
        return res
    
    def maximumStrength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] = p[i] + nums[i]
        self.cache = {}
        return self.msum(p, 0, 2 * k, -1)