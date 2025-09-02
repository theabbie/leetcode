class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        mod = 10**9 + 7
        def toBase(x, b):
            if x == 0:
                return [0]
            arr = []
            while x:
                arr.append(x % b)
                x //= b
            return arr[::-1]
        def countUp(x):
            if x < 0:
                return 0
            dig = toBase(x, b)
            n = len(dig)
            @cache
            def dp(pos, tight, started, last):
                if pos == n:
                    return 1
                res = 0
                up = dig[pos] if tight else b - 1
                for d in range(up + 1):
                    nt = tight and (d == up)
                    if not started:
                        if d == 0:
                            res += dp(pos + 1, nt, False, 0)
                        else:
                            res += dp(pos + 1, nt, True, d)
                    else:
                        if d >= last:
                            res += dp(pos + 1, nt, True, d)
                return res % mod
            return dp(0, True, False, 0)
        L = int(l)
        R = int(r)
        return (countUp(R) - countUp(L - 1)) % mod