"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root:
            mdepth = 1
            if root.children:
                for c in root.children:
                    curr = 1 + self.maxDepth(c)
                    mdepth = max(mdepth, curr)
            return mdepth
        return 0