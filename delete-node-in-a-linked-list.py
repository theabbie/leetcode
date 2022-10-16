class Solution:
    def deleteNode(self, node):
        prev = node
        curr = node
        while curr and curr.next:
            curr.val = curr.next.val
            prev = curr
            curr = curr.next
        prev.next = None