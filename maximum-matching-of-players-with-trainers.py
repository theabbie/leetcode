class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        n = len(players)
        players.sort()
        trainers.sort()
        i = 0
        for t in trainers:
            if i < n and t >= players[i]:
                i += 1
        return i