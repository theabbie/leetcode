class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        ctr = [0] * 26
        for w in words:
            for c in w:
                ctr[ord(c) - ord('a')] += 1
        for i in ctr:
            if i % n != 0:
                return False
        return True