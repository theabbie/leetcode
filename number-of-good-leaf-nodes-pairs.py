from sortedcontainers import SortedList

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        res = 0
        def dfs(r, d):
            nonlocal res
            leaf = True
            curr = SortedList()
            for c in [r.left, r.right]:
                if not c:
                    continue
                leaf = False
                ncurr = dfs(c, d + 1)
                if len(ncurr) > len(curr):
                    curr, ncurr = ncurr, curr
                for x in ncurr:
                    res += curr.bisect_right(distance + 2 * d - x)
                while ncurr:
                    x = ncurr.pop(0)
                    curr.add(x)
            if leaf:
                curr.add(d)
            return curr
        dfs(root, 0)
        return res