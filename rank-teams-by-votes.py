class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes)
        m = len(votes[0])
        ctr = [[0] * m for _ in range(26)]
        for i in range(n):
            for j in range(m):
                ctr[ord(votes[i][j]) - ord('A')][j] -= 1
        return "".join(sorted(votes[0], key = lambda c: (ctr[ord(c) - ord('A')], c)))