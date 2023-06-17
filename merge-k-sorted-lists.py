import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        heap = []
        head = None
        curr = None
        for i in range(n):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
        while len(heap) > 0:
            currval, i = heapq.heappop(heap)
            if not head:
                head = lists[i]
                curr = head
            else:
                curr.next = lists[i]
                curr = curr.next
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
        return head