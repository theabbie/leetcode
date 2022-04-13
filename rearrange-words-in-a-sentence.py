class Solution:
    def arrangeWords(self, text: str) -> str:
        op =  " ".join(sorted(text.lower().split(), key = lambda s: len(s)))
        return op[0].upper() + op[1:]