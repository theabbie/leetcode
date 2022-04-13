class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ss = ""
        tt = ""
        for c in s:
            if c == "#":
                ss = ss[:-1]
            else:
                ss += c
        for c in t:
            if c == "#":
                tt = tt[:-1]
            else:
                tt += c
        return ss == tt