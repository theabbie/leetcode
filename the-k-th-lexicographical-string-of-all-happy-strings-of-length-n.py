class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        @lru_cache(None)
        def getcount(i, prev):
            if i >= n:
                return 1
            ctr = 0
            for x in range(3):
                if x != prev:
                    ctr += getcount(i + 1, x)
            return ctr
        if getcount(0, -1) < k:
            return ""
        res = []
        for i in range(n):
            for c in range(3):
                if len(res) > 0 and c == res[-1]:
                    continue
                curr = getcount(i + 1, c)
                if curr >= k:
                    res.append(c)
                    break
                else:
                    k -= curr
        return "".join(chr(ord('a') + x) for x in res)