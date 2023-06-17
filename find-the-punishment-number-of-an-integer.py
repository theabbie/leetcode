class Solution:
    def valid(self, num, i, val, cache):
        n = len(num)
        if i == n:
            return val == 0
        key = (i, val)
        if key in cache:
            return cache[key]
        curr = 0
        for j in range(i, n):
            curr = 10 * curr + num[j]
            if self.valid(num, j + 1, val - curr, cache):
                cache[key] = True
                return True
        cache[key] = False
        return False
    
    def punishmentNumber(self, n: int) -> int:
        res = 0
        for i in range(1, n + 1):
            if self.valid(list(map(int, str(i * i))), 0, i, {}):
                res += i * i
        return res