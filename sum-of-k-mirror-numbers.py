def gen(b, n, m=40):
    c = 0
    s = 0
    for l in range(1, m + 1):
        h = (l + 1) // 2
        a = b ** (h - 1)
        e = b ** h
        for p in range(a, e):
            d = []
            t = p
            for _ in range(h):
                d.append(t % b)
                t //= b
            d = d[::-1]
            if l % 2 == 0:
                q = d + d[::-1]
            else:
                q = d + d[-2::-1]
            v = 0
            for x in q:
                v = v * b + x
            if str(v) == str(v)[::-1]:
                s += v
                c += 1
                if c >= n:
                    return s

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        return gen(k, n)