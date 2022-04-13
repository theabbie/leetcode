import heapq

class Solution:
    def kSmallestPairs(self, nums1, nums2, k: int):
        heap = []
        a = min(len(nums1), k)
        b = min(len(nums2), k)
        for i in range(a):
            for j in range(b):
                heapq.heappush(heap, (-nums1[i]-nums2[j], (nums1[i], nums2[j])))
                if len(heap) > k:
                    heapq.heappop(heap)
        ksmallest = []
        for i in range(k):
            if len(heap) > 0:
                ksmallest.insert(0, list(heapq.heappop(heap)[1]))
        return ksmallest