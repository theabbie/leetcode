from collections import *
import heapq

class Heap:
    def __init__(self):
        self.heap = []
        self.deleted = defaultdict(int)

    def push(self, val):
        heapq.heappush(self.heap, val)

    def clean(self):
        while len(self.heap) > 0 and self.heap[0] in self.deleted:
            self.deleted[self.heap[0]] -= 1
            if self.deleted[self.heap[0]] == 0:
                del self.deleted[self.heap[0]]
            heapq.heappop(self.heap)

    def __len__(self):
        self.clean()
        return len(self.heap)
    
    def min(self):
        self.clean()
        return self.heap[0]
    
    def __repr__(self):
        return str(self.deleted)
    
    def delete(self, val):
        self.deleted[val] += 1

    def pop(self):
        self.clean()
        return heapq.heappop(self.heap)
    
class FenwickTree:
    def __init__(self, x):
        self.bit = x
        for i in range(len(x)):
            j = i | (i + 1)
            if j < len(x):
                x[j] += x[i]

    def update(self, idx, x):
        while idx < len(self.bit):
            self.bit[idx] += x
            idx |= idx + 1

    def query(self, end):
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

n, d, w = map(int, input().split())

apples = []

maxt = 0

for _ in range(n):
    t, x = map(int, input().split())
    apples.append((x, t))
    maxt = max(maxt, t)

apples.sort()

times = FenwickTree([0] * (maxt + 1))

msum = Heap()

i = 0

res = 0

sums = defaultdict(list)

def addtime(tm):
    ctr = getcount(tm)
    for s in sums[(tm, ctr)]:
        msum.delete(s)
    sums[(tm, ctr)] = []
    l = times.query(tm + 1) - times.query(max(tm - d, 0))
    r = times.query(min(tm + d + 1, maxt)) - times.query(tm)
    msum.push(l)
    msum.push(r)
    ctr = getcount(tm)
    sums[(tm, ctr)].append(l)
    sums[(tm, ctr)].append(r)

def deltime(tm):
    ctr = getcount(tm)
    for s in sums[(tm, ctr)]:
        msum.delete(s)
    sums[(tm, ctr)] = []
    l = times.query(tm + 1) - times.query(max(tm - d, 0))
    r = times.query(min(tm + d + 1, maxt)) - times.query(tm)
    msum.delete(l)
    msum.delete(r)
    ctr = getcount(tm)
    sums[(tm, ctr)].append(l)
    sums[(tm, ctr)].append(r)

def getcount(tm):
    return times.query(tm + 1) - times.query(tm)

for j in range(n):
    deltime(apples[j][1])
    times.update(apples[j][1], 1)
    addtime(apples[j][1])
    while i < j and apples[j][0] - apples[i][0] > w:
        deltime(apples[i][1])
        times.update(apples[i][1], -1)
        addtime(apples[i][1])
        i += 1
    if len(msum) > 0:
        res = max(res, -msum.min())

print(res)