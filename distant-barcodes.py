import bisect

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        n = len(barcodes)
        ctr = {}
        for b in barcodes:
            ctr[b] = ctr.get(b, 0) + 1
        freq = sorted([(-v, k) for k, v in ctr.items()])
        op = []
        while len(op) < n:
            i = 0
            curr = freq[i]
            if len(op) > 0:
                while curr[1] == op[-1]:
                    i += 1
                    curr = freq[i]
                c = curr[1]
            else:
                c = curr[1]
            op.append(c)
            del freq[bisect.bisect_left(freq, curr)]
            if curr[0] + 1 < 0:
                bisect.insort(freq, (curr[0] + 1, curr[1]))
        return op