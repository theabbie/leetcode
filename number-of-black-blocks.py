class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        res = [0] * 5
        res[0] = (m - 1) * (n - 1)
        cc = {}
        for a, b in coordinates:
            cc[(a, b)] = 1
        v = set()
        for a, b in coordinates:
            for dx in range(-1, 1):
                for dy in range(-1, 1):
                    if (a + dx, b + dy) in v:
                        continue
                    v.add((a + dx, b + dy))
                    curr = 0
                    total = 0
                    for x in range(a + dx, a + dx + 2):
                        for y in range(b + dy, b + dy + 2):
                            if 0 <= x < m and 0 <= y < n:
                                total += 1
                                curr += cc.get((x, y), 0)
                    if total == 4:
                        res[curr] += 1
                        res[0] -= 1
        return res