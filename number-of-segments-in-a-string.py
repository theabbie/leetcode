class Solution:
    def countSegments(self, s: str) -> int:
        prev = None
        ctr = 0
        for c in s:
            if (prev == None or prev == " ") and c != " ":
                ctr += 1
            prev = c
        return ctr