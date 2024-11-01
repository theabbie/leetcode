import heapq

class Solution:
    def countGreatEnoughNodes(self, root: Optional[TreeNode], k: int) -> int:
        res = 0
        def dfs(r):
            nonlocal res
            curr = []
            if not r:
                return curr
            for lval in dfs(r.left):
                heapq.heappush(curr, lval)
            for rval in dfs(r.right):
                heapq.heappush(curr, rval)
            while len(curr) > k:
                heapq.heappop(curr)
            if len(curr) == k and r.val > -curr[0]:
                res += 1
            heapq.heappush(curr, -r.val)
            return curr
        dfs(root)
        return res