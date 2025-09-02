class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def check(seq):
            n = len(seq)
            dp = [[set() for _ in range(n)] for _ in range(n)]
            for i in range(n):
                dp[i][i].add(float(seq[i]))
            for length in range(2, n+1):
                for l in range(n - length + 1):
                    r = l + length - 1
                    for k in range(l, r):
                        for x in dp[l][k]:
                            for y in dp[k+1][r]:
                                dp[l][r].add(x + y)
                                dp[l][r].add(x - y)
                                dp[l][r].add(y - x)
                                dp[l][r].add(x * y)
                                if abs(y) > 1e-9:
                                    dp[l][r].add(x / y)
                                if abs(x) > 1e-9:
                                    dp[l][r].add(y / x)
            return any(abs(v - 24) < 1e-6 for v in dp[0][n-1])
        
        for p in permutations(cards):
            if check(p):
                return True
        return False