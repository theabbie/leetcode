class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        s += "0"
        segments = []
        chunk = ""
        for c in s:
            if c == '0' and len(chunk) > 0:
                segments.append(chunk)
                chunk = ""
            elif c == '1':
                chunk += '1'
        return len(segments) <= 1