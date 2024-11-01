class Solution:
    def minimumSteps(self, s: str) -> int:
        res = o = 0
        for c in s:
            if c == "0":
                res += o
            else:
                o += 1
        return res