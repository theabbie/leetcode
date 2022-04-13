import heapq

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    nodes = {}
    
    def traverse(self, root, w, h):
        if root:
            self.traverse(root.left, w - 1, h + 1)
            self.nodes[w] = self.nodes.get(w, []) + [(h, root.val)]
            self.traverse(root.right, w + 1, h + 1)
    
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        op = []
        self.nodes = {}
        self.traverse(root, 0, 0)
        heap = [(w, n) for w, n in self.nodes.items()]
        heapq.heapify(heap)
        while len(heap) > 0:
            w, n = heapq.heappop(heap)
            n.sort()
            op.append([item[1] for item in n])
        return op