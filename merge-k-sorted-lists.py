import heapq

class Solution:
    def merge(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        else:
            l2.next = self.merge(l1, l2.next)
            return l2
    
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        l = lambda x: 0 if not x else 1 + l(x.next)
        heap = []
        for i, el in enumerate(lists):
            heapq.heappush(heap, (l(el), i))
        while len(heap) > 1:
            la, a = heapq.heappop(heap)
            lb, b = heapq.heappop(heap)
            lists.append(self.merge(lists[a], lists[b]))
            heapq.heappush(heap, (la + lb, len(lists) - 1))
        return lists[heap[0][1]]