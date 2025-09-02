from collections import deque

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n & 1:
            return False
        opens = []
        extra = []
        for i in range(n):
            if locked[i] == '0':
                extra.append(i)
                continue
            if s[i] == '(':
                opens.append(i)
            else:
                if opens:
                    opens.pop()
                elif extra:
                    extra.pop()
                else:
                    return False
        while opens:
            x = opens.pop()
            if not extra:
                return False
            if extra[-1] < x:
                return False
            extra.pop()
        return len(extra) % 2 == 0