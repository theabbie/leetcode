class Solution:
    def copy(self, head):
        newhead = None
        if head:
            newhead = self.visited.get(head, Node(head.val))
            self.visited[head] = newhead
            if head.random != None:
                newhead.random = self.visited.get(head.random, Node(head.random.val))
                self.visited[head.random] = newhead.random
            newhead.next = self.copy(head.next)
        return newhead
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        self.visited = {}
        return self.copy(head)