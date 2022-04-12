class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = {}
        for a, b in edges:
            indegree[b] = indegree.get(b, 0) + 1
        return [i for i in range(n) if i not in indegree]