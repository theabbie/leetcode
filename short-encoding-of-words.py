class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = set(words)
        deleted = set()
        for word in words:
            n = len(word)
            for j in range(1, n):
                curr = word[-j:]
                if curr in words:
                    deleted.add(curr)
        for word in deleted:
            words.remove(word)
        return len(words) + sum([len(w) for w in words])