class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = " " + s
        n = len(s)
        chunk = ""
        for i in range(n - 1, -1, -1):
            if s[i] == " ":
                if len(chunk) > 0:
                    return len(chunk)
            else:
                chunk += s[i]