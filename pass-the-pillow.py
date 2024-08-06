class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        i = 1
        f = True
        for _ in range(time):
            if i == 1:
                f = True
            if i == n:
                f = False
            if f:
                i += 1
            else:
                i -= 1
        return i