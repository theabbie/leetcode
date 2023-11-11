class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        words = set()
        for s in startWords:
            ctr = [0] * 26
            for c in s:
                ctr[ord(c) - ord('a')] += 1
            words.add(tuple(ctr))
        res = 0
        for w in targetWords:
            ctr = [0] * 26
            for c in w:
                ctr[ord(c) - ord('a')] += 1
            for i in range(26):
                if ctr[i] != 1:
                    continue
                ctr[i] -= 1
                if tuple(ctr) in words:
                    res += 1
                    break
                ctr[i] += 1
        return res