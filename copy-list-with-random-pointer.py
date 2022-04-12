"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copy(self, head):
        newhead = None
        if head:
            newhead = self.visited.get(head.val, Node(head.val))
            self.visited[newhead.val] = newhead
            if head.random != None:
                newhead.random = self.visited.get(head.random.val, Node(head.random.val))
                self.visited[newhead.random.val] = newhead.random
            newhead.next = self.copy(head.next)
        return newhead
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        self.visited = {}
        i = 0
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr.val = i
            curr = curr.next
            i += 1
        newhead = self.copy(head)
        i = 0
        curr = newhead
        while curr:
            curr.val = vals[i]
            curr = curr.next
            i += 1
        return newhead