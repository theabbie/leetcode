class Solution:
    def canWin(self, nums, i, j, ascore, bscore, aturn):
        if i > j:
            if aturn:
                return ascore >= bscore
            return bscore > ascore
        if aturn:
            return not self.canWin(nums, i + 1, j, ascore + nums[i], bscore, False) or not self.canWin(nums, i, j - 1, ascore + nums[j], bscore, False)
        return not self.canWin(nums, i + 1, j, ascore, bscore + nums[i], True) or not self.canWin(nums, i, j - 1, ascore, bscore + nums[j], True)
    
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        return self.canWin(nums, 0, n - 1, 0, 0, True)