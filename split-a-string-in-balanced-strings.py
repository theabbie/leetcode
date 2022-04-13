class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ctr = 0
        curr = 0
        for c in s:
            if curr == 0:
                ctr += 1
            if c == 'L':
                curr += 1
            else:
                curr -= 1
        if curr == 0:
            ctr += 1
        return ctr - 1