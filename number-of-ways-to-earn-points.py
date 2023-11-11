M = 10 ** 9 + 7

class Solution:
    def count(self, types, i, n, used, rem):
        if rem < 0:
            return 0
        if i >= n:
            return int(rem == 0)
        key = (i, used, rem)
        if key in self.cache:
            return self.cache[key]
        res = 0
        if used < types[i][0]:
            res += self.count(types, i, n, used + 1, rem - types[i][1])
        res += self.count(types, i + 1, n, 0, rem)
        res %= M
        self.cache[key] = res
        return res
    
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        self.cache = {}
        return self.count(types, 0, len(types), 0, target)