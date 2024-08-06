class Solution:
    def leafSeq(self, root):
        seq = []
        nodes = [root]
        while len(nodes) > 0:
            curr = nodes.pop()
            if curr:
                if not curr.left and not curr.right:
                    seq.append(curr.val)
                nodes.append(curr.left)
                nodes.append(curr.right)
        return seq
    
    def leafSimilar(self, root1, root2):
        return self.leafSeq(root1) == self.leafSeq(root2)