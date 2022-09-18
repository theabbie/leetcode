class Solution:
    def isPalindrome(self, ctr):
        odds = 0
        for el in ctr:
            if el % 2 == 1:
                odds += 1
        return odds <= 1
    
    def inorder(self, root, ctr):
        if root:
            ctr[root.val] += 1
            self.inorder(root.left, ctr)
            self.inorder(root.right, ctr)
            if not root.left and not root.right:
                if self.isPalindrome(ctr):
                    self.res += 1
            ctr[root.val] -= 1
    
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        ctr = [0] * 10
        self.res = 0
        self.inorder(root, ctr)
        return self.res