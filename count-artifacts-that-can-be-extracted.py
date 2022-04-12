class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        ogctr = {}
        currctr = {}
        afmap = {}
        for i, af in enumerate(artifacts):
            a, b, c, d = af
            for x in range(a, c + 1):
                for y in range(b, d + 1):
                    ogctr[i] = ogctr.get(i, 0) + 1
                    afmap[(x, y)] = i
        for x, y in dig:
            if (x, y) in afmap:
                af = afmap[(x, y)]
                currctr[af] = currctr.get(af, 0) + 1
        ctr = 0
        for af in currctr:
            if currctr.get(af, 0) == ogctr.get(af, 0):
                ctr += 1
        return ctr