class Solution:
    def topologicalSort(self, graph, node, visited, stack, pos):
        visited.add(node)
        for n in graph.get(node, []):
            if n not in visited:
                self.topologicalSort(graph, n, visited, stack, pos)
        if node in pos:
            stack.append(pos[node])
    
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = {}
        supplies = set(supplies)
        n = len(recipes)
        for i in range(n):
            for item in ingredients[i]:
                graph[item] = graph.get(item, []) + [recipes[i]]
        pos = {}
        for i, item in enumerate(recipes):
            pos[item] = i
        stack = []
        visited = set()
        for node in graph:
            if node not in visited:
                self.topologicalSort(graph, node, visited, stack, pos)
        for i in stack[::-1]:
            valid = True
            for item in ingredients[i]:
                if item not in supplies:
                    valid = False
                    break
            if valid:
                supplies.add(recipes[i])
            else:
                recipes[i] = False
        return [r for r in recipes if r]