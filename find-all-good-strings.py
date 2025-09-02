MOD = 10 ** 9 + 7

def count_strings_with_constraints(upper, sub):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    M = len(sub)
    N = len(upper)

    prefix = [0] * M
    for i in range(1, M):
        j = prefix[i - 1]
        while j > 0 and sub[j] != sub[i]:
            j = prefix[j - 1]
        if sub[j] == sub[i]:
            j += 1
        prefix[i] = j

    dp = [[[0] * 2 for _ in range(M)] for _ in range(N + 1)]
    dp[0][0][1] = 1

    for i in range(1, N + 1):
        for j in range(M):
            for t in range(2):
                if dp[i - 1][j][t] > 0:
                    limit = upper[i - 1] if t == 1 else 'z'
                    for c in alphabet:
                        if c > limit:
                            break

                        k = j
                        while k > 0 and sub[k] != c:
                            k = prefix[k - 1]
                        if sub[k] == c:
                            k += 1

                        if k < M:
                            dp[i][k][t and (c == limit)] = (dp[i][k][t and (c == limit)] + dp[i - 1][j][t]) % MOD

    return sum((dp[N][j][0] + dp[N][j][1]) % MOD for j in range(M)) % MOD

class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        return (count_strings_with_constraints(s2, evil) - count_strings_with_constraints(s1, evil) + int(evil not in s1)) % MOD