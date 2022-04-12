import heapq

class Solution:
    def tallestBillboard(self, rods):
        n = len(rods)
        lens = {}
        for mask in range(1 << n):
            currlen = 0
            curr = set()
            for i in range(n):
                if mask & (1 << i):
                    curr.add(i)
                    currlen += rods[i]
            lens[currlen] = lens.get(currlen, []) + [curr]
        heap = [(-k, v) for k, v in lens.items() if len(v) > 1]
        heapq.heapify(heap)
        while len(heap) > 0:
            size, sets = heapq.heappop(heap)
            k = len(sets)
            for i in range(k):
                for j in range(i + 1, k):
                    if len(set.intersection(sets[i], sets[j])) == 0:
                        return -size
        return 0

print(Solution().tallestBillboard([1,2,4,8,16,32,64,128,256,512,50,50,50,150,150,150,100,100,100,123]))