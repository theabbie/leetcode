class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        res = 0
        for i in range(len(s)):
            a = ord(s[i]) - ord('a')
            b = ord(t[i]) - ord('a')
            f = 0
            while a != b:
                f += nextCost[a]
                a += 1
                a %= 26
            a = ord(s[i]) - ord('a')
            b = ord(t[i]) - ord('a')
            l = 0
            while a != b:
                l += previousCost[a]
                a -= 1
                a %= 26
            res += min(f, l)
        return res