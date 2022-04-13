class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        s += "x"
        longest = [0, 0]
        curr = [0, 0]
        for c in s:
            if c == "x":
                longest[0] = max(longest[0], curr[0])
                longest[1] = max(longest[1], curr[1])
            elif c == "1":
                longest[0] = max(longest[0], curr[0])
                curr[0] = 0
                curr[1] += 1
            elif c == "0":
                longest[1] = max(longest[1], curr[1])
                curr[1] = 0
                curr[0] += 1
        return longest[1] > longest[0]