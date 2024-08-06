class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        s = {0}
        rewardValues.sort()
        for el in rewardValues:
            s |= {x + el for x in s if el > x}
        return max(s)