class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        k = n - k
        currSum = sum(cardPoints[:k])
        minSum = currSum
        for i in range(n - k):
            currSum = currSum - cardPoints[i] + cardPoints[i + k]
            minSum = min(minSum, currSum)
        return sum(cardPoints) - minSum