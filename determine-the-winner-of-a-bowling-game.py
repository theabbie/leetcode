class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        n = len(player1)
        a = 0
        b = 0
        for i in range(n):
            actr = 0
            for j in [i - 2, i - 1]:
                if j >= 0 and player1[j] == 10:
                    actr += 1
            bctr = 0
            for j in [i - 2, i - 1]:
                if j >= 0 and player2[j] == 10:
                    bctr += 1
            if actr == 0:
                a += player1[i]
            else:
                a += 2 * player1[i]
            if bctr == 0:
                b += player2[i]
            else:
                b += 2 * player2[i]
        if a > b:
            return 1
        elif b > a:
            return 2
        else:
            return 0