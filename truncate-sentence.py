class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        op = ""
        ctr = 0
        for c in s:
            if c == " ":
                ctr += 1
                if ctr == k:
                    return op
            op += c
        return op