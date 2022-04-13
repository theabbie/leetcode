class Solution:
    def maxPower(self, s: str) -> int:
        s += "0"
        maxCtr = [0] * 26
        curr = [0] * 26
        for c in s:
            for i in range(26):
                maxCtr[i] = max(maxCtr[i], curr[i])
            if c != "0":
                tmp = curr[ord(c) - ord('a')]
                curr = [0] * 26
                curr[ord(c) - ord('a')] = tmp
                curr[ord(c) - ord('a')] += 1
        return max(maxCtr)