from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        graph = defaultdict(list)
        for a, b in tickets:
            graph[a].append(b)
        res = ["JFK"]
        def DFS(curr):
            if len(res) == len(tickets) + 1:
                return True
            if len(graph[curr]) == 0:
                return False
            nb = list(graph[curr])
            for i, v in enumerate(nb):
                res.append(v)
                graph[curr].pop(i)
                if DFS(v):
                    return True
                graph[curr].insert(i, v)
                res.pop()
        DFS("JFK")
        return res