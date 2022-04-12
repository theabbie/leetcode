class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = [set(w) for w in text.split()]
        broken = set(brokenLetters)
        return len([w for w in words if len(set.intersection(w, broken)) == 0])