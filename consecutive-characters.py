class Solution:
    def maxPower(self, s: str) -> int:
        s += "0"
        maxCtr = [0] * 26
        curr = [0] * 26
        for c in s:
            for i in range(26):
                maxCtr[i] = max(maxCtr[i], curr[i])
            if c != "0":
                k = ord(c) - ord('a')
                curr = [0 if i != k else curr[i] for i in range(26)]
                curr[k] += 1
        return max(maxCtr)