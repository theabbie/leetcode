class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        n = len(s)
        lens = [0] * n
        lens[0] = 1
        for i in range(1, n):
            if s[i].isdigit():
                lens[i] = int(s[i]) * lens[i - 1]
            else:
                lens[i] = lens[i - 1] + 1
        def getChar(s, i, pos):
            if s[i].isdigit():
                return getChar(s, i - 1, pos % lens[i - 1])
            if pos + 1 == lens[i]:
                return s[i]
            return getChar(s, i - 1, pos)
        return getChar(s, n - 1, k - 1)