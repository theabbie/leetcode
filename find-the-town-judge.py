class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustedGraph = {}
        trustingGraph = {}
        for a, b in trust:
            trustedGraph[b] = trustedGraph.get(b, 0) + 1
            trustingGraph[a] = trustingGraph.get(a, 0) + 1
        for i in range(1, n + 1):
            if trustedGraph.get(i, 0) == n - 1 and trustingGraph.get(i, 0) == 0:
                return i
        return -1