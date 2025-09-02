class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        n = len(word)
        res = [n - i for i in range(n + 1)]
        forbidden = set(forbidden)
        for l in {len(s) for s in forbidden}:
            for i in range(n - l + 1):
                if word[i:i+l] in forbidden:
                    res[i] = min(res[i], l - 1)
        for i in range(n - 1, -1, -1):
            res[i] = min(res[i], 1 + res[i + 1])
        return max(res)