class Solution:
    def countPoints(self, rings: str) -> int:
        n = len(rings)
        rods = [set(), set(), set()]
        for i in range(0, n, 2):
            if rings[i] == 'R':
                rods[0].add(int(rings[i + 1]))
            if rings[i] == 'G':
                rods[1].add(int(rings[i + 1]))
            if rings[i] == 'B':
                rods[2].add(int(rings[i + 1]))
        return len(set.intersection(*rods))