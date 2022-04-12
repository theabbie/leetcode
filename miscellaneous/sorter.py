class Solution:
    def topologicalSort(self, graph, node, visited, stack):
        visited.add(node)
        for n in graph.get(node, []):
            if n not in visited:
                self.topologicalSort(graph, n, visited, stack)
        stack.append(node)

    def sort(self, arr):
        n = len(arr)
        graph = {}
        for i in range(n):
            for j in range(n):
                if j != i and arr[j] >= arr[i]:
                    graph[i] = graph.get(i, []) + [j]
        visited = set()
        stack = []
        for item in graph:
            if item not in visited:
                self.topologicalSort(graph, item, visited, stack)
        stack.reverse()
        return stack

print(Solution().sort([3,5,7,9,11,6,3,6]))
