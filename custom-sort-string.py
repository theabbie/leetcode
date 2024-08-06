class Solution:
    def customSortString(self, order: str, s: str) -> str:
        pos = {}
        for i in range(len(order)):
            pos[order[i]] = i
        return "".join(sorted(s, key = lambda x: pos.get(x, -1)))