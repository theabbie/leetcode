class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        res = []
        x = 0
        for c in word:
            x = 10 * x + int(c)
            x %= m
            res.append(int(x == 0))
        return res