class Solution:
    def topologicalSort(self, graph, node, visited, stack):
        visited.add(node)
        for n in graph.get(node, []):
            if n not in visited:
                self.topologicalSort(graph, n, visited, stack)
        stack.append(node)
    
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = {}
        supplies = set(supplies)
        op = []
        n = len(recipes)
        for i in range(n):
            for item in ingredients[i]:
                graph[item] = graph.get(item, []) + [recipes[i]]
        stack = []
        visited = set()
        for node in graph:
            if node not in visited:
                self.topologicalSort(graph, node, visited, stack)
        stack.reverse()
        pos = {}
        for i, item in enumerate(recipes):
            pos[item] = i
        for curr in stack:
            if curr in pos:
                i = pos[curr]
                valid = True
                for item in ingredients[i]:
                    if item not in supplies:
                        valid = False
                        break
                if valid:
                    supplies.add(recipes[i])
                    op.append(recipes[i])
        return op