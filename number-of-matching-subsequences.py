class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        n = len(s)
        last = {}
        nextpos = [None] * (n + 1)
        nextpos[n] = {}
        for i in range(n - 1, -1, -1):
            last[s[i]] = i
            nextpos[i] = dict(last)
        res = 0
        for w in words:
            prev = -1
            res += 1
            for c in w:
                if c in nextpos[prev + 1]:
                    prev = nextpos[prev + 1][c]
                else:
                    res -= 1
                    break
        return res