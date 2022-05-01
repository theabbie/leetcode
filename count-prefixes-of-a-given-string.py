class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        n = len(s)
        prefixes = set()
        for i in range(1, n + 1):
            prefixes.add(s[:i])
        ctr = 0
        for w in words:
            if w in prefixes:
                ctr += 1
        return ctr