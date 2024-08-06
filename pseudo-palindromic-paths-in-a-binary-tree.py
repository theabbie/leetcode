target = {0}
for i in range(9):
    target.add(1 << i)

class Solution:
    def inorder(self, root, ctr):
        if root:
            ctr ^= 1 << root.val - 1
            self.inorder(root.left, ctr)
            self.inorder(root.right, ctr)
            if not root.left and not root.right:
                if ctr in target:
                    self.res += 1
    
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.inorder(root, 0)
        return self.res