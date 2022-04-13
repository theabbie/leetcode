class Solution:
    def countTriples(self, n: int) -> int:
        exists = set()
        for c in range(1, n + 1):
            exists.add(c * c)
        ctr = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if (a * a + b * b) in exists:
                    ctr += 1
        return ctr