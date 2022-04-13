class Solution:
    def binaryGap(self, n: int) -> int:
        curr = "{:b}".format(n)
        n = len(curr)
        mdist = 0
        prev = -1
        for i in range(n):
            if curr[i] == "1":
                if prev >= 0:
                    mdist = max(mdist, i - prev)
                prev = i
        return mdist