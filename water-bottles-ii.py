class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        full = numBottles
        empty = 0
        ex = numExchange
        res = 0
        while True:
            res += full
            empty += full
            full = 0
            if ex > empty:
                break
            empty -= ex
            full += 1
            ex += 1
        return res