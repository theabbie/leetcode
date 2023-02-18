class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        n = len(colors)
        i = 0
        a = b = 0
        while i < n:
            ctr = 1
            while i < n - 1 and colors[i] == colors[i + 1]:
                i += 1
                ctr += 1
            if colors[i] == 'A':
                a += max(ctr - 2, 0)
            else:
                b += max(ctr - 2, 0)
            i += 1
        return a > b