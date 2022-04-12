import heapq

class Solution:
    def rearrangeBarcodes(self, barcodes):
        n = len(barcodes)
        ctr = {}
        for b in barcodes:
            ctr[b] = ctr.get(b, 0) + 1
        op = []
        while len(op) < n:
            heap = [(-v, k) for k, v in ctr.items()]
            heapq.heapify(heap)
            curr = heapq.heappop(heap)
            if len(op) > 0:
                while curr[1] == op[-1]:
                    curr = heapq.heappop(heap)
                c = curr[1]
            else:
                c = curr[1]
            op.append(c)
            ctr[c] -= 1
            if ctr[c] == 0:
                del ctr[c]
        return op

print(Solution().rearrangeBarcodes([1,1,1,1,2,2,3,3]))