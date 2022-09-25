class Solution:
    def inorder(self, root, path, rem):
        if root:
            path.append(root.val)
            rem -= root.val
            self.inorder(root.left, path, rem)
            self.inorder(root.right, path, rem)
            if not root.left and not root.right and rem == 0:
                self.res.append(path[:])
            path.pop()
           
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []
        self.inorder(root, [], targetSum)
        return self.res