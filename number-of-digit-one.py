class Solution:
    def digitone(self, curr, i, n, val, tight, cache):
        if i >= n:
            return curr
        key = (curr, i, tight)
        if key in cache:
            return cache[key]
        res = 0
        maxd = 9
        if tight:
            maxd = int(val[i])
        for d in range(maxd + 1):
            currtight = False
            if d == maxd:
                currtight = tight
            x = 0
            if d == 1:
                x += 1
            res += self.digitone(curr + x, i + 1, n, val, currtight, cache)
        if not tight:
            cache[key] = res
        return res
    
    def countDigitOne(self, n: int) -> int:
        val = str(n)
        l = len(val)
        return self.digitone(0, 0, l, val, True, {})