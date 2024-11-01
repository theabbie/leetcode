def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            node = ListNode(gcd(curr.val, curr.next.val))
            curr.next, node.next = node, curr.next
            curr = curr.next.next
        return head