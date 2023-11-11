from itertools import permutations

class Solution:
    def merge(self, x, y):
        if y in x:
            return x
        res = 0
        for i in range(1, min(len(x), len(y))):
            if x[-i:] == y[:i]:
                res = i
        return x + y[res:]
    
    def minimumString(self, a: str, b: str, c: str) -> str:
        res = (float('inf'), "")
        for perm in permutations([a, b, c]):
            curr = ""
            for s in perm:
                curr = self.merge(curr, s)
            res = min(res, (len(curr), curr))
        return res[1]