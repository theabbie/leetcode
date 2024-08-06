class Solution:
    def minsteps(self, key, i, pos, j, l):
        if i >= len(key):
            return 0
        if (i, j) in self.cache:
            return self.cache[(i, j)]
        res = float('inf')
        for k in pos[key[i]]:
            cost = abs(k - j)
            cost = min(cost, l - cost) + 1
            res = min(res, cost + self.minsteps(key, i + 1, pos, k, l))
        self.cache[(i, j)] = res
        return res
    
    def findRotateSteps(self, ring: str, key: str) -> int:
        self.cache = {}
        pos = defaultdict(list)
        for i, c in enumerate(ring):
            pos[c].append(i)
        return self.minsteps(key, 0, pos, 0, len(ring))