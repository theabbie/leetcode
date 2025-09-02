class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        f = Counter()
        for el in basket1:
            f[el] += 1
        for el in basket2:
            f[el] -= 1
        for el in f.values():
            if el & 1:
                return -1
        v = []
        for el, c in sorted(f.items()):
            v.extend([el] * (abs(c) // 2))
        if not v:
            return 0
        m = min(f)
        return sum(min(2 * m, x) for x in v[:len(v)//2])