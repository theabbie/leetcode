class Solution:
    def topologicalSort(self, graph, node, visited, stack):
        visited.add(node)
        for n in graph.get(node, []):
            if n not in visited:
                self.topologicalSort(graph, n, visited, stack)
        stack.append(node)
    
    def findAllRecipes(self, recipes, ingredients, supplies):
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
        for val in stack:
            valid = True
            for item in ingredients[i]:
                if item not in supplies:
                    print(recipes[i], item)
                    valid = False
                    break
            if valid:
                supplies.add(recipes[i])
                op.append(recipes[i])
        return op

print(Solution().findAllRecipes(["xevvq","izcad","p","we","bxgnm","vpio","i","hjvu","igi","anp","tokfq","z","kwdmb","g","qb","q","b","hthy"],
[["wbjr"],["otr","fzr","g"],["fzr","wi","otr","xgp","wbjr","igi","b"],["fzr","xgp","wi","otr","tokfq","izcad","igi","xevvq","i","anp"],["wi","xgp","wbjr"],["wbjr","bxgnm","i","b","hjvu","izcad","igi","z","g"],["xgp","otr","wbjr"],["wbjr","otr"],["wbjr","otr","fzr","wi","xgp","hjvu","tokfq","z","kwdmb"],["xgp","wi","wbjr","bxgnm","izcad","p","xevvq"],["bxgnm"],["wi","fzr","otr","wbjr"],["wbjr","wi","fzr","xgp","otr","g","b","p"],["otr","fzr","xgp","wbjr"],["xgp","wbjr","q","vpio","tokfq","we"],["wbjr","wi","xgp","we"],["wbjr"],["wi"]],
["wi","otr","wbjr","fzr","xgp"]))