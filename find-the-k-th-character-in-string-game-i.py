class Solution:
    def kthCharacter(self, k: int) -> str:
        s = "a"
        def nxt(c):
            c = ord(c) - ord('a')
            c += 1
            c %= 26
            return chr(ord('a') + c)
        while len(s) < k:
            s += "".join(nxt(c) for c in s)
        return s[k-1]