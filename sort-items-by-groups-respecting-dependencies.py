from collections import defaultdict, deque, Counter

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        groups = defaultdict(set)
        extra = m
        for i in range(n):
            if group[i] != -1:
                groups[group[i]].add(i)
            else:
                groups[extra].add(i)
                group[i] = extra
                extra += 1
        graph = defaultdict(lambda: defaultdict(set))
        groupgraph = defaultdict(set)
        for j in range(n):
            for i in beforeItems[j]:
                graph[i][group[j]].add(j)
                if group[i] != group[j]:
                    groupgraph[group[i]].add(group[j])
        gindegree = Counter()
        for g in groupgraph:
            for j in groupgraph[g]:
                gindegree[j] += 1
        res = defaultdict(list)
        for g in groups:
            indegree = Counter()
            for i in groups[g]:
                for j in graph[i][g]:
                    indegree[j] += 1
            q = deque()
            for i in groups[g]:
                if indegree[i] == 0:
                    q.appendleft(i)
            while len(q) > 0:
                curr = q.pop()
                res[g].append(curr)
                for j in graph[curr][g]:
                    indegree[j] -= 1
                    if indegree[j] == 0:
                        q.appendleft(j)
        order = []
        q = deque()
        for g in groups:
            if gindegree[g] == 0:
                q.appendleft(g)
        while len(q) > 0:
            curr = q.pop()
            order.extend(res[curr])
            for j in groupgraph[curr]:
                gindegree[j] -= 1
                if gindegree[j] == 0:
                    q.appendleft(j)
        if len(order) < n:
            return []
        return order