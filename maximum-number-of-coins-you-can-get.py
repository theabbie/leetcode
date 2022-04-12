class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort()
        score = 0
        i = 0
        j = n
        while j - i >= 3:
            score += piles[j - 2]
            i += 1
            j -= 2
        return score