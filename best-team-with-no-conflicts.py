class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        seq = sorted(range(n), key = lambda i: (ages[i], scores[i]))
        scores = [scores[seq[i]] for i in range(n)]
        scores.append(float('inf'))
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n + 1):
                if scores[j] >= scores[i]:
                    dp[i] = max(dp[i], scores[i] + dp[j])
        return max(dp)