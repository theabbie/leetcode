class Solution:
    def dfs(self, root, upper, k, target):
        if not root:
            return float('inf')
        d = float('inf')
        if root.val == target.val:
            d = 0
            upper = k
        l = 1 + self.dfs(root.left, upper - 1, k, target)
        r = 1 + self.dfs(root.right, upper - 1, k, target)
        if l == k or r == k or upper == 0:
            self.res.append(root.val)
        if l < float('inf'):
            self.dfs(root.right, k - l - 1, k, target)
        if r < float('inf'):
            self.dfs(root.left, k - r - 1, k, target)
        return min(d, l, r)
    
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.res = []
        self.dfs(root, float('inf'), k, target)
        return self.res