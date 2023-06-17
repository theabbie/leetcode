class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        f = [1] * (n + 1)
        for i in range(1, n + 1):
            f[i] = i * f[i - 1]
        res = []
        used = set()
        for i in range(n):
            for d in range(1, n + 1):
                if d in used:
                    continue
                if k > f[n - i - 1]:
                    k -= f[n - i - 1]
                else:
                    used.add(d)
                    res.append(str(d))
                    break
        return "".join(res)