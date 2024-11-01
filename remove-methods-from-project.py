class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        rgraph = [[] for _ in range(n)]
        for a, b in invocations:
            graph[a].append(b)
            rgraph[b].append(a)
        bad = {k}
        stack = [k]
        while stack:
            i = stack.pop()
            for j in graph[i]:
                if j not in bad:
                    bad.add(j)
                    stack.append(j)
        for i in bad:
            for j in rgraph[i]:
                if j not in bad:
                    return list(range(n))
        return [i for i in range(n) if i not in bad]