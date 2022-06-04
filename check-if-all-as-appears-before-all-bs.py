class Solution:
    def checkString(self, s: str) -> bool:
        bseen = False
        for c in s:
            if c == 'b':
                bseen = True
            if c == 'a':
                if bseen:
                    return False
        return True