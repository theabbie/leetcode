class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        for m in moves:
            if m == "U":
                y += 1
            elif m == "D":
                y -= 1
            elif m == "R":
                x += 1
            elif m == "L":
                x -= 1
        return (x, y) == (0, 0)