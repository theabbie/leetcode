class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        ranks = sorted(range(n), key = lambda i: -score[i])
        labels = {
            0: "Gold Medal",
            1: "Silver Medal",
            2: "Bronze Medal"
        }
        op = [0] * n
        for i, r in enumerate(ranks):
            op[r] = labels.get(i, str(i + 1))
        return op