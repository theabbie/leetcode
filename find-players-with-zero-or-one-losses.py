import bisect
from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        played = defaultdict(int)
        won = defaultdict(int)
        for winner, loser in matches:
            won[winner] += 1
            played[winner] += 1
            played[loser] += 1
        answer = [[], []]
        for player in played:
            lost = played[player] - won[player]
            if lost == 0:
                bisect.insort(answer[0], player)
            elif lost == 1:
                bisect.insort(answer[1], player)
        return answer