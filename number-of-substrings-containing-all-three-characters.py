import bisect

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        a = []
        b = []
        c = []
        for i in range(n):
            if s[i] == "a":
                a.append(i)
            elif s[i] == "b":
                b.append(i)
            else:
                c.append(i)
        a.append(n)
        b.append(n)
        c.append(n)
        res = n * n
        for i in range(n):
            apos = bisect.bisect_left(a, i)
            bpos = bisect.bisect_left(b, i)
            cpos = bisect.bisect_left(c, i)
            pos = max(a[apos], b[bpos], c[cpos])
            res -= pos
        return res