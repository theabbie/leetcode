class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)
        return left + right + [root.val]