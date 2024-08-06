class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        s = needle + "#" + haystack
        n = len(s)
        Z = [0] * n
        l = r = 0
        for i in range(1, n):
            z = Z[i - l]
            if i + z >= r:
                z = max(r - i, 0)
                while i + z < n and s[z] == s[i + z]:
                    z += 1
                l, r = i, i + z
            Z[i] = z
            if i > len(needle) and z >= len(needle):
                return i - len(needle) - 1
        return -1