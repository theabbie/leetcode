class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            mid = ListNode(self.gcd(curr.val, curr.next.val))
            mid.next = curr.next
            curr.next = mid
            curr = mid.next
        return head