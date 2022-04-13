from collections import Counter

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [Counter("qwertyuiop"), Counter("asdfghjkl"), Counter("zxcvbnm")]
        op = []
        for word in words:
            isValid = False
            for ctr in rows:
                valid = len([c for c in word if ctr[c.lower()] == 0]) == 0
                if valid:
                    isValid = True
                    break
            if isValid:
                op.append(word)
        return op