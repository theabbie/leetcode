class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        T = minutesToTest // minutesToDie
        x = 0
        while (T + 1) ** x < buckets:
            x += 1
        return x