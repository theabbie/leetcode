class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)
        val = lambda c: ord(c) - ord('a') + 1
        p = 1
        powers = []
        for _ in range(k):
            powers.append(p)
            p = (p * power) % modulo
        curr = 0
        for i in range(k):
            curr = (curr + val(s[n - k + i]) * powers[i]) % modulo
        res = None
        for i in range(n - k - 1, -1, -1):
            if curr == hashValue:
                res = s[i + 1 : i + k + 1]
            curr = (power * (curr + modulo - (val(s[i + k]) * powers[k - 1]) % modulo) + val(s[i])) % modulo
        if curr == hashValue:
            res = s[:k]
        return res
            