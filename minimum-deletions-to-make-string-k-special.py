class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        n = len(word)
        ctr = Counter(word)
        res = float('inf')
        for minf in range(1, n + 1):
            maxf = minf + k
            curr = 0
            for c in ctr:
                if ctr[c] < minf:
                    curr += ctr[c]
                if ctr[c] > maxf:
                    curr += ctr[c] - maxf
            res = min(res, curr)
        return res