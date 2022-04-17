from collections import defaultdict

class Solution:
    def longest(self, tree, root, s, branch):
        l = 1
        key = (root, branch)
        if key in self.cache:
            return self.cache[key]
        if branch:
            best = 0
            sbest = 0
            for j in tree[root]:
                if s[root] != s[j]:
                    currl = self.longest(tree, j, s, False)
                    sbest, best = sorted([sbest, best, currl])[-2:]
            l = max(l, 1 + best + sbest)
            self.cache[key] = l
            return l
        for j in tree[root]:
            if s[root] != s[j]:
                currl = self.longest(tree, j, s, False)
                l = max(l, 1 + currl)
        self.cache[key] = l
        return l
    
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(s)
        self.cache = {}
        tree = defaultdict(list)
        for i in range(n):
            if parent[i] != -1:
                tree[parent[i]].append(i)
        mpath = 0
        for i in range(n):
            l = self.longest(tree, i, s, True)
            mpath = max(mpath, l)
        return mpath