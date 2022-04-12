# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getTrees(self, beg, end):
        trees = []
        
        if beg > end:
            trees.append(None)
            return trees

        for i in range(beg, end + 1):
            left_subtrees = self.getTrees(beg, i - 1)
            right_subtrees = self.getTrees(i + 1, end)

            for l in left_subtrees:
                for r in right_subtrees:
                    tree = TreeNode(val = i, left = l, right = r)
                    trees.append(tree)
        return trees
    
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.getTrees(1, n)