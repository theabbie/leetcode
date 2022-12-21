from collections import defaultdict

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(set)
        for a, b in dislikes:
            graph[a - 1].add(b - 1)
            graph[b - 1].add(a - 1)
        stack = []
        color = [None] * n
        v = set()
        for i in graph:
            if i not in v:
                v.add(i)
                stack.append(i)
                color[i] = 0
                while len(stack) > 0:
                    curr = stack.pop()
                    for j in graph[curr]:
                        if color[j] != None and color[j] == color[curr]:
                            return False
                        if j not in v:
                            v.add(j)
                            stack.append(j)
                            color[j] = 1 - color[curr]
        return True