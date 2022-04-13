class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        n = len(s)
        i = 0
        op = []
        while i < n:
            ctr = 1
            while i < n - 1 and s[i] == s[i + 1]:
                ctr += 1
                i += 1
            i += 1
            if ctr >= 3:
                op.append([i - ctr, i - 1])
        return op