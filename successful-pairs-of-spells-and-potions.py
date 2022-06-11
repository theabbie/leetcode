import bisect

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(potions)
        potions.sort()
        return [n - bisect.bisect_left(potions, success / sp) for sp in spells]