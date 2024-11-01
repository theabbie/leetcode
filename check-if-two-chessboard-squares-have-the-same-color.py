class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        s = lambda p: (ord(p[0]) - ord('a') + int(p[1]) - 1) % 2
        return s(coordinate1) == s(coordinate2)