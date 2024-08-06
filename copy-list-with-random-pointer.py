class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodecache = {}
        def clone(curr):
            if not curr:
                return curr
            if curr in nodecache:
                return nodecache[curr]
            copy = Node(curr.val)
            nodecache[curr] = copy
            copy.next = clone(curr.next)
            copy.random = clone(curr.random)
            return copy
        return clone(head)