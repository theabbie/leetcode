class Solution:
    def getNum(self, graph, i, res):
        if res[i] != -1:
            return res[i]
        mval = 0
        for j in graph[i]:
            curr = self.getNum(graph, j, res)
            mval = max(mval, curr)
        res[i] = 1 + mval
        return 1 + mval
    
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        graph = {}
        for i in range(n):
            graph[i] = []
            l = float('inf')
            r = float('inf')
            if i > 0:
                l = ratings[i - 1]
            if i < n - 1:
                r = ratings[i + 1]
            if ratings[i] > l:
                graph[i].append(i - 1)
            if ratings[i] > r:
                graph[i].append(i + 1)
        res = [-1] * n
        for i in range(n):
            self.getNum(graph, i, res)
        return sum(res)