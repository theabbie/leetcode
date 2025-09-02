class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        s = list(s)
        p = 0
        for i in range(len(s) - 1, -1, -1):
            p += shifts[i]
            s[i] = chr(ord('a') + (ord(s[i]) - ord('a') + p) % 26)
        return "".join(s)