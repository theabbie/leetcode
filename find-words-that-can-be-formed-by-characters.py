from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars = Counter(chars)
        l = 0
        for w in words:
            curr = Counter(w)
            possible = True
            for c in curr:
                if chars[c] < curr[c]:
                    possible = False
                    break
            if possible:
                l += len(w)
        return l