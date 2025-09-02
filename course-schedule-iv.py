class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(n)]
        for u, v in prerequisites:
            graph[u].append(v)
        @cache
        def check(x, y):
            if x == y:
                return True
            for z in graph[x]:
                if check(z, y):
                    return True
            return False
        return [check(u, v) for u, v in queries]