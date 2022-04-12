class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        z = 0
        o = 0
        zeroes = [z]
        ones = [o]
        for c in s:
            if c == '0':
                z += 1
            if c == '1':
                o += 1
            zeroes.append(z)
            ones.append(o)
        ways = 0
        for i in range(n):
            if s[i] == '0':
                ways += (ones[i] - ones[0]) * (ones[-1] - ones[i + 1])
            elif s[i] == '1':
                ways += (zeroes[i] - zeroes[0]) * (zeroes[-1] - zeroes[i + 1])
        return ways