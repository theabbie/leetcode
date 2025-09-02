class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:
        from functools import cache
        valid_sums = {}
        for s in range(1, 82):
            temp = s
            cnt2 = cnt3 = cnt5 = cnt7 = 0
            for p in (2, 3, 5, 7):
                while temp % p == 0:
                    if p == 2:
                        cnt2 += 1
                    elif p == 3:
                        cnt3 += 1
                    elif p == 5:
                        cnt5 += 1
                    else:
                        cnt7 += 1
                    temp //= p
            if temp == 1:
                valid_sums[s] = (cnt2, cnt3, cnt5, cnt7)
        fac = {0: None, 1: (0, 0, 0, 0), 2: (1, 0, 0, 0), 3: (0, 1, 0, 0), 4: (2, 0, 0, 0), 5: (0, 0, 1, 0), 6: (1, 1, 0, 0), 7: (0, 0, 0, 1), 8: (3, 0, 0, 0), 9: (0, 2, 0, 0)}
        def count(n):
            s_n = str(n)
            N = len(s_n)
            @cache
            def dp(pos, tight, started, zero_flag, s_val, a, b, c, d):
                if pos == N:
                    if not started or s_val == 0:
                        return 0
                    if zero_flag:
                        return 1
                    if s_val not in valid_sums:
                        return 0
                    r2, r3, r5, r7 = valid_sums[s_val]
                    return 1 if (a >= r2 and b >= r3 and c >= r5 and d >= r7) else 0
                res = 0
                up = int(s_n[pos]) if tight else 9
                for dig in range(up + 1):
                    ntight = tight and (dig == up)
                    if not started:
                        if dig == 0:
                            res += dp(pos + 1, ntight, False, False, 0, 0, 0, 0, 0)
                        else:
                            nf = fac[dig]
                            res += dp(pos + 1, ntight, True, False, dig, nf[0], nf[1], nf[2], nf[3])
                    else:
                        ns = s_val + dig
                        if zero_flag or dig == 0:
                            res += dp(pos + 1, ntight, True, True, ns, 0, 0, 0, 0)
                        else:
                            nf = fac[dig]
                            res += dp(pos + 1, ntight, True, False, ns, a + nf[0], b + nf[1], c + nf[2], d + nf[3])
                return res
            return dp(0, True, False, False, 0, 0, 0, 0, 0)
        return count(r) - (count(l - 1) if l else 0)