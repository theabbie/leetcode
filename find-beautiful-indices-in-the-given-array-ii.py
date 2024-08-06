def find_pattern_indices(s, p):
    s = p + "#" + s
    n = len(s)
    Z = [0] * n
    l = r = 0
    for i in range(1, n):
        z = Z[i - l]
        if i + z >= r:
            z = max(r - i, 0)
            while i + z < n and s[z] == s[i + z]:
                z += 1
            l, r = i, i + z
        Z[i] = z
        if i > len(p) and z >= len(p):
            yield i - len(p) - 1

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        n = len(s)
        x = find_pattern_indices(s, a)
        y = find_pattern_indices(s, b)
        val = [0] * (n + 1)
        for i in y:
            val[i] = 1
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] = p[i] + val[i]
        res = []
        for i in x:
            ctr = p[min(i + k + 1, n)] - p[max(i - k, 0)]
            if ctr > 0:
                res.append(i)
        return res 