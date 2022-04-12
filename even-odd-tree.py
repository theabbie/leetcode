# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
        return [levels[l] for l in range(level + 1)]
    
    def isOddAndIncreasing(self, arr):
        n = len(arr)
        for i in range(n - 1):
            if arr[i] >= arr[i + 1] or arr[i] % 2 == 0:
                return False
        if arr[-1] % 2 == 0:
            return False
        return True
    
    def isEvenAndDecreasing(self, arr):
        n = len(arr)
        for i in range(n - 1):
            if arr[i] <= arr[i + 1] or arr[i] % 2 == 1:
                return False
        if arr[-1] % 2 == 1:
            return False
        return True
    
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        levels = self.levelOrder(root)
        for i, level in enumerate(levels):
            if i % 2 == 0 and not self.isOddAndIncreasing(level):
                return False
            elif i % 2 == 1 and not self.isEvenAndDecreasing(level):
                return False
        return True