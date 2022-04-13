class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s) + [""]
        chunk = ""
        op = ""
        for c in s:
            if c == " " or c == "":
                op += chunk[::-1]
                op += c
                chunk = ""
            else:
                chunk += c
        return op