class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        ranks = sorted(range(n), key = lambda i: -score[i])
        labels = {
            0: "Gold Medal",
            1: "Silver Medal",
            2: "Bronze Medal"
        }
        return [labels.get(ranks.index(i), str(ranks.index(i) + 1)) for i in range(n)]