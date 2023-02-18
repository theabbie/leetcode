class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        p = [0] * (n + 1)
        for i in range(n):
            k = 0
            if words[i][0] in "aeiou" and words[i][-1] in "aeiou":
                k = 1
            p[i + 1] += p[i] + k
        return [p[r + 1] - p[l] for l, r in queries]