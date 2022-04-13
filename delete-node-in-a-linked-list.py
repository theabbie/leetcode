# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        prev = node
        curr = node
        while curr and curr.next:
            curr.val = curr.next.val
            prev = curr
            curr = curr.next
        prev.next = None