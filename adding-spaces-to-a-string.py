class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        s = list(s)
        for i in spaces:
            s[i] = " " + s[i]
        return "".join(s)