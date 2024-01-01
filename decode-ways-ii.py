M = 10 ** 9 + 7

class Solution:
    def count(self, s, i, l, n):
        ctr = 0
        if s[i] == '0':
            return ctr
        key = s[i:i+l]
        if key in self.cache:
            return self.cache[key]
        for x in range(1, 27):
            x = str(x)
            if len(x) != l:
                continue
            valid = True
            for j in range(len(x)):
                if i + j >= n:
                    valid = False
                    break
                if s[i + j] != '*' and s[i + j] != x[j]:
                    valid = False
                    break
                if s[i + j] == '*' and x[j] == '0':
                    valid = False
                    break
            if valid:
                ctr += 1
        self.cache[key] = ctr
        return ctr
    
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 2)
        dp[n] = 1
        self.cache = {}
        for i in range(n - 1, -1, -1):
            dp[i] += self.count(s, i, 1, n) * dp[i + 1]
            dp[i] += self.count(s, i, 2, n) * dp[i + 2]
            dp[i] %= M
        return dp[0]