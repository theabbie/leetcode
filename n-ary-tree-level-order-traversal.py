"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        nodes = [(root, 0)]
        i = 0
        op = {}
        while i < len(nodes):
            curr, level = nodes[i]
            if curr:
                op[level] = op.get(level, []) + [curr.val]
                for node in curr.children:
                    nodes.append((node, level + 1))
            i += 1
        return list(op.values())