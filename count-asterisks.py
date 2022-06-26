class Solution:
    def countAsterisks(self, s: str) -> int:
        ctr = 0
        stars = 0
        for c in s:
            if c == '|':
                ctr += 1
            if c == '*' and ctr % 2 == 0:
                stars += 1
        return stars