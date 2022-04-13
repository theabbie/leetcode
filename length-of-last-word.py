class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s += " "
        latest = None
        chunk = ""
        for c in s:
            if c == " ":
                if len(chunk) > 0:
                    latest = chunk
                chunk = ""
            else:
                chunk += c
        return len(latest)