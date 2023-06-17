"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def DFS(self, grid, a, b, l):
        root = Node(val = 1)
        currsum = 0
        ctr = 0
        for i in range(a, a + l):
            for j in range(b, b + l):
                currsum += grid[i][j]
                ctr += 1
        if currsum == 0 or currsum == ctr:
            root.isLeaf = True
            root.val = 0 if currsum == 0 else 1
        else:
            root.topLeft = self.DFS(grid, a, b, l // 2)
            root.topRight = self.DFS(grid, a, b + l // 2, l // 2)
            root.bottomLeft = self.DFS(grid, a + l // 2, b, l // 2)
            root.bottomRight = self.DFS(grid, a + l // 2, b + l // 2, l // 2)
        return root
    
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        return self.DFS(grid, 0, 0, n)