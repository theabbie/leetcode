import heapq

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        heap = []
        paths = [root1, root2]
        i = 0
        while i < len(paths):
            curr = paths[i]
            if curr:
                heapq.heappush(heap, curr.val)
                if curr.left:
                    paths.append(curr.left)
                if curr.right:
                    paths.append(curr.right)
            i += 1
        return heapq.nsmallest(len(heap), heap)