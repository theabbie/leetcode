class Solution:
    def longestWord(self, words: List[str]) -> str:
        words = set(words)
        mword = ""
        for word in words:
            n = len(word)
            valid = True
            for i in range(1, n):
                if word[:i] not in words:
                    valid = False
                    break
            if valid:
                if len(word) > len(mword):
                    mword = word
                elif len(word) == len(mword) and word < mword:
                    mword = word
        return mword