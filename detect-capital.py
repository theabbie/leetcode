class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        caps = 0
        for i in range(n):
            if word[i].isupper():
                caps += 1
        if caps == 0 or caps == n:
            return True
        if caps == 1 and word[0].isupper():
            return True
        return False