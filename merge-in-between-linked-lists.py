class Solution:
    def getNode(self, head, k):
        while k:
            if not head.next and k < 0:
                break
            head = head.next
            k -= 1
        return head
    
    def mergeInBetween(self, list1, a, b, list2):
        curr = self.getNode(list2, -1)
        curr.next = self.getNode(list1, b + 1)
        beg = self.getNode(list1, a - 1)
        beg.next = list2
        return list1