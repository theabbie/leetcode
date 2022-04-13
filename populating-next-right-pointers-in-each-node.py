"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        paths = [(root, 0)]
        i = 0
        latest = (0, -1)
        while i < len(paths):
            curr, level = paths[i]
            if curr:
                if level == latest[1]:
                    curr.next = latest[0]
                latest = paths[i]
                paths.append((curr.right, level + 1))
                paths.append((curr.left, level + 1))
            i += 1
        return root
            
# class Solution:
#     def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
#         if root and root.left and root.right:
#             root.left.next = root.right
#             root.left = self.connect(root.left)
#             root.right = self.connect(root.right)
#         return root