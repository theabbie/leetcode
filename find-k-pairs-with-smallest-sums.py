import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m = len(nums1)
        n = len(nums2)
        heap = [(nums1[0] + nums2[0], 0, 0)]
        res = []
        v = {(0, 0)}
        while len(heap) > 0 and k > 0:
            val, i, j = heapq.heappop(heap)
            res.append((nums1[i], nums2[j]))
            k -= 1
            for x, y in [(i + 1, j), (i, j + 1)]:
                if x < m and y < n:
                    if (x, y) not in v:
                        v.add((x, y))
                        heapq.heappush(heap, (nums1[x] + nums2[y], x, y))
        return res