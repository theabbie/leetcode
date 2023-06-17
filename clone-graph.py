class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        nodemap = {}
        nodemap[node.val] = Node(val = node.val)
        paths = [node]
        while len(paths) > 0:
            curr = paths.pop()
            currcopy = nodemap[curr.val]
            for nbr in curr.neighbors:
                if nbr.val not in nodemap:
                    paths.append(nbr)
                    nodemap[nbr.val] = Node(val = nbr.val)
                currcopy.neighbors.append(nodemap[nbr.val])
        return nodemap[node.val]