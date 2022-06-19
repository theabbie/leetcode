# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCam(self, root: Optional[TreeNode], id, isMonitored = False) -> int:
        minCams = float('inf')
        if root:
            if (id, isMonitored) in self.cache:
                return self.cache[(id, isMonitored)]
            lum = self.minCam(root.left, 2 * id, isMonitored = False)
            rum = self.minCam(root.right, 2 * id + 1, isMonitored = False)
            lm = self.minCam(root.left, 2 * id, isMonitored = True)
            rm = self.minCam(root.right, 2 * id + 1, isMonitored = True)
            minCams = min(minCams, 1 + lm + rm)
            if not isMonitored:
                if root.left:
                    ll = self.minCam(root.left.left, 4 * id, isMonitored = True)
                    lr = self.minCam(root.left.right, 4 * id + 1, isMonitored = True)
                    minCams = min(minCams, 1 + rum + ll + lr)
                if root.right:
                    rl = self.minCam(root.right.left, 4 * id + 2, isMonitored = True)
                    rr = self.minCam(root.right.right, 4 * id + 3, isMonitored = True)
                    minCams = min(minCams, 1 + lum + rl + rr)
            else:
                minCams = min(minCams, lum + rum)
            self.cache[(id, isMonitored)] = minCams
            return minCams
        return 0
    
    def minCameraCover(self, root: Optional[TreeNode], allowRoot = True) -> int:
        self.cache = {}
        return self.minCam(root, 1, isMonitored = False)