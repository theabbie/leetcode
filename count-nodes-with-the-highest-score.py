from collections import defaultdict

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        tree = defaultdict(set)
        root = None
        for i in range(n):
            if parents[i] != -1:
                tree[parents[i]].add(i)
            else:
                root = i
        def DFS(tree, root, sums):
            res = 1
            for j in tree[root]:
                res += DFS(tree, j, sums)
            sums[root] = res
            return res
        sums = {}
        DFS(tree, root, sums)
        mscore = 0
        mctr = 0
        stack = [root]
        while len(stack) > 0:
            curr = stack.pop()
            currscore = max(sums[root] - sums[curr], 1)
            for j in tree[curr]:
                stack.append(j)
                currscore *= sums[j]
            if currscore > mscore:
                mscore = currscore
                mctr = 1
            elif currscore == mscore:
                mctr += 1
        return mctr