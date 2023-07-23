from collections import defaultdict, deque, Counter

class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        n = len(parent)
        graph = defaultdict(set)
        for i in range(1, n):
            graph[parent[i]].add((i, s[i]))
        masks = []
        q = deque([(0, 0)])
        while len(q) > 0:
            curr, cmask = q.pop()
            masks.append(cmask)
            for j, c in graph[curr]:
                q.appendleft((j, cmask ^ (1 << (ord(c) - ord('a')))))
        res = 0
        for target in [0] + [(1 << c) for c in range(26)]:
            ctr = Counter()
            for el in masks:
                res += ctr[el ^ target]
                ctr[el] += 1
        return res