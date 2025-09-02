class Solution:
    def canAliceWin(self, n: int) -> bool:
        s = 0
        prev = 10
        res = True
        while s <= n:
            s += prev
            prev -= 1
            res = not res
        return res