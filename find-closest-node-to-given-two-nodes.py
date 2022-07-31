from collections import deque

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        res = []
        for beg in [node1, node2]:
            q = deque([(beg, 0)])
            v = {beg}
            dists = {}
            while len(q) > 0:
                curr, d = q.pop()
                dists[curr] = d
                if edges[curr] != -1 and edges[curr] not in v:
                    v.add(edges[curr])
                    q.appendleft((edges[curr], d + 1))
            res.append(dists)
        minnode = None
        mindist = float('inf')
        for i in range(n):
            currdist = max(res[0].get(i, float('inf')), res[1].get(i, float('inf')))
            if currdist < mindist:
                mindist = currdist
                minnode = i
            elif currdist == mindist:
                if minnode == None or i < minnode:
                    minnode = i
        if minnode == None or mindist == float('inf'):
            return -1
        return minnode