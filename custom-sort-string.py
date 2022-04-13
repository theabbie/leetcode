class Solution:
    def customSortString(self, order: str, s: str) -> str:
        pos = {}
        for i, c in enumerate(order):
            pos[c] = i
        return "".join(sorted(s, key = lambda c: pos.get(c, 0)))