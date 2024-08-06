from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodecache = {}
        def clone(i):
            if not i:
                return i
            if i.val in nodecache:
                return nodecache[i.val]
            copy = Node(i.val)
            nodecache[copy.val] = copy
            for j in i.neighbors:
                copy.neighbors.append(clone(j))
            return copy
        return clone(node)