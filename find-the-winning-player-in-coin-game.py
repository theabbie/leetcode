class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        w = True
        while x >= 1 and y >= 4:
            x -= 1
            y -= 4
            w = not w
        return "Bob" if w else "Alice"