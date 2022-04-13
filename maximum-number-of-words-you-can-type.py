class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        return len([True for w in text.split() if len(set.intersection(set(w), broken)) == 0])