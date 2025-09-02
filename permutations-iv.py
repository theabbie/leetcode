class Solution:
    def permute(self, n: int, k: int) -> List[int]:
        def cnt(a, b, r):
            if a + b == 0:
                return 1
            if r is None:
                if a == b:
                    return 2 * math.factorial(a) * math.factorial(b)
                elif a == b + 1 or b == a + 1:
                    return math.factorial(a) * math.factorial(b)
                else:
                    return 0
            else:
                if r == 1:
                    if (a + b) % 2 == 0:
                        if a != b:
                            return 0
                    else:
                        if a != b + 1:
                            return 0
                    return math.factorial(a) * math.factorial(b)
                else:
                    if (a + b) % 2 == 0:
                        if a != b:
                            return 0
                    else:
                        if b != a + 1:
                            return 0
                    return math.factorial(a) * math.factorial(b)

        o = [x for x in range(1, n + 1) if x % 2]
        e = [x for x in range(1, n + 1) if not x % 2]
        if k > cnt(len(o), len(e), None):
            return []
        r = []
        req = None
        for _ in range(n):
            c = sorted(o + e) if req is None else (o if req == 1 else e)
            f = False
            for x in c:
                if x % 2:
                    nr = 0
                    na = len(o) - 1
                    nb = len(e)
                else:
                    nr = 1
                    na = len(o)
                    nb = len(e) - 1
                cval = cnt(na, nb, nr)
                if k > cval:
                    k -= cval
                else:
                    r.append(x)
                    (o if x % 2 else e).remove(x)
                    req = nr
                    f = True
                    break
            if not f:
                return []
        return r