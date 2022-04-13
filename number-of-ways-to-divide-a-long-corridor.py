class Solution:
    def numberOfWays(self, corridor: str) -> int:
        if corridor.count("S") % 2 != 0:
            return 0
        ctr = 0
        pos = []
        for i, c in enumerate(corridor):
            if c == "S":
                if ctr == 0:
                    pos.append(i)
                ctr += 1
            if ctr == 2:
                pos.append(i)
                ctr = 0
        if len(pos) <= 1:
            return 0
        if len(pos) == 2:
            return 1
        p = 1
        n = len(pos)
        for i in range(1, n, 2):
            if i < n and i + 1 < n:
                p *= (pos[i + 1] - pos[i])
        return p % ((10 ** 9) + 7)