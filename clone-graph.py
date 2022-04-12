"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        nodemap = {}
        nodemap[node] = Node(val = node.val)
        paths = [node]
        while len(paths) > 0:
            curr = paths.pop()
            currcopy = nodemap[curr]
            for nbr in curr.neighbors:
                if nbr in nodemap:
                    currcopy.neighbors.append(nodemap[nbr])
                else:
                    paths.append(nbr)
                    nodemap[nbr] = Node(val = nbr.val)
                    currcopy.neighbors.append(nodemap[nbr])
        return nodemap[node]