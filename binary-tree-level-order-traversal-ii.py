# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [(root, 0)]
        levels = {}
        level = 0
        while len(queue) > 0:
            curr, level = queue.pop(0)
            levels[level] = levels.get(level, []) + [curr.val]
            if curr.left:
                queue.append((curr.left, level + 1))
            if curr.right:
                queue.append((curr.right, level + 1))
        return [levels[l] for l in range(level, -1, -1)]