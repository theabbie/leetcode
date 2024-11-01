class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        if n == 1:
            return len([i for i in range(1, 10) if i % k == 0])
        vals = set()
        res = 0
        for i in range(1, pow(10, n // 2)):
            i = str(i)
            pals = [int(i + i[::-1])]
            for d in range(10):
                pals.append(int(i + str(d) + i[::-1]))
            for val in pals:
                if len(str(val)) == n and val % k == 0:
                    ctr = [0] * 10
                    for _ in range(n):
                        ctr[val % 10] += 1
                        val //= 10
                    vals.add(tuple(ctr))
        f = [1] * (n + 1)
        for i in range(1, n + 1):
            f[i] = i * f[i - 1]
        for val in vals:
            curr = f[n]
            for c in val:
                curr //= f[c]
            if val[0] > 0:
                sub = f[n - 1]
                for i in range(10):
                    sub //= (f[val[i]] if i > 0 else f[val[i] - 1])
                curr -= sub
            res += curr
        return res