from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ctrNote = Counter(ransomNote)
        ctrMag = Counter(magazine)
        for c in ctrNote:
            if ctrMag[c] < ctrNote[c]:
                return False
        return True