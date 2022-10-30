from collections import defaultdict

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        dp = defaultdict(int)
        def preorder(root, h):
            if root:
                dp[root.val] = max(dp[root.val], self.maxheight)
                self.maxheight = max(self.maxheight, h)
                preorder(root.left, h + 1)
                preorder(root.right, h + 1)
        def preorderrev(root, h):
            if root:
                dp[root.val] = max(dp[root.val], self.maxheight)
                self.maxheight = max(self.maxheight, h)
                preorderrev(root.right, h + 1)
                preorderrev(root.left, h + 1)
        self.maxheight = 0
        preorder(root, 0)
        self.maxheight = 0
        preorderrev(root, 0)
        res = []
        for q in queries:
            res.append(dp[q])
        return res