class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        n = len(words)
        prev = [[float('inf')] * 26 for _ in range(26)]
        res = sum(len(w) for w in words)
        for i in range(n):
            k = len(words[i])
            f = ord(words[i][0]) - ord('a')
            l = ord(words[i][-1]) - ord('a')
            if i == 0:
                prev[f][l] = k
                continue
            curr = [[float('inf')] * 26 for _ in range(26)]
            for a in range(26):
                for b in range(26):
                    curr[f][b] = min(curr[f][b], k + prev[a][b] - int(a == l))
                    curr[a][l] = min(curr[a][l], k + prev[a][b] - int(b == f))
                    if i == n - 1:
                        res = min(res, curr[f][b], curr[a][l])
            curr, prev = prev, curr
        return res