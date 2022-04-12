class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[b] = graph.get(b, []) + [a]
            indegree[a] += 1
        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        ctr = 0
        while len(queue) > 0:
            curr = queue.pop(0)
            for j in graph.get(curr, []):
                indegree[j] -= 1
                if indegree[j] == 0:
                    queue.append(j)
            ctr += 1
        if ctr < numCourses:
            return False
        return True