class Solution:
    def stoneGameRec(self, score, oppscore, piles):
        if len(piles) == 1:
            if score + piles[0] > oppscore:
                return True
        if not self.stoneGameRec(score + piles[0], oppscore, piles[1:]) and not self.stoneGameRec(score + piles[-1], oppscore, piles[:-1]):
            return False
        return True
    
    def stoneGame(self, piles: List[int]) -> bool:
        return self.stoneGameRec(0, 0, piles)