class Solution:
    def alienOrder(self, words: List[str]) -> str:
        indegree = Counter()
        for s in words:
            for c in s:
                indegree[c] = 0
        graph = defaultdict(set)
        for i in range(len(words) - 1):
            j = 0
            while j < len(words[i]) and j < len(words[i + 1]) and words[i][j] == words[i + 1][j]:
                j += 1
            if j < len(words[i]):
                if j == len(words[i + 1]):
                    return ""
                graph[words[i][j]].add(words[i + 1][j])
        for a in graph:
            for b in graph[a]:
                indegree[b] += 1
        q = deque()
        for c in indegree:
            if indegree[c] == 0:
                q.appendleft(c)
        res = []
        while q:
            i = q.pop()
            res.append(i)
            for j in graph[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.appendleft(j)
        if len(res) < len(indegree):
            return ""
        return "".join(res)