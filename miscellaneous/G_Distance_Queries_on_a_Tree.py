from collections import defaultdict, deque
import sys

sys.setrecursionlimit(10 ** 7)
 
class LazySegmentTree:
    def __init__(self, data, padding = 0):
        """initialize the lazy segment tree with data"""
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()
        
        self.data = [padding] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(1, _size)):
            self.data[i] = self.data[2 * i] + self.data[2 * i + 1]     
        self._lazy = [1,0] * (2 * _size)
 
    def _push(self, idx):
        """push query on idx to its children"""
        # Let the children know of the queries
        idx *= 2
        a = self._lazy[idx]
        b = self._lazy[idx + 1] >> 1
        self._lazy[idx] = 1
        self._lazy[idx + 1] = 0
        
        self.data[idx] = a * self.data[idx] + b
        self.data[idx + 1] = a * self.data[ idx + 1] + b
        
        idx *= 2
        self._lazy[idx] = a * self._lazy[idx] 
        self._lazy[idx + 1] = a * self._lazy[idx + 1] + b
        self._lazy[idx + 2] = a * self._lazy[idx + 2]
        self._lazy[idx + 3] = a * self._lazy[idx + 3] + b
    
    def _build(self, idx):
        """make the changes to idx be known to its ancestors"""
        idx >>= 1
        while idx:
            # TODO
            self.data[idx] = self.data[2 * idx] + self.data[2 * idx + 1]
            idx >>= 1
 
    def _update(self, idx):
        """updates the node idx to know of all queries applied to it via its ancestors"""
        for i in reversed(range(1, idx.bit_length())):
            self._push(idx >> i)
 
    def add(self, start, stop, val):
        """lazily add value to [start, stop)"""
        a, b = val
        start = start_copy = start + self._size
        stop = stop_copy = stop + self._size
 
        # Apply all the lazily stored queries
        self._update(start); self._update(stop - 1)
 
        while start < stop:
            if start & 1:
                self.data[start] = a * self.data[start] + b
                self._lazy[2 * start] = a * self._lazy[2 * start]
                self._lazy[2 * start + 1] = a * self._lazy[2 * start + 1] + b
                start += 1
            if stop & 1:
                stop -= 1
                self.data[stop] = a * self.data[stop] + b
                self._lazy[2 * stop] = a * self._lazy[2 * stop]
                self._lazy[2 * stop + 1] = a * self._lazy[2 * stop + 1] + b
            start >>= 1; stop >>= 1; b <<= 1
        
        while not start_copy&1: start_copy >>= 1
        while not stop_copy&1: stop_copy >>= 1
        self._build(start_copy); self._build(stop_copy - 1)
 
    def query(self, start, stop, res = float('inf')):
        """func of data[start, stop)"""
        start += self._size; stop += self._size
 
        # Apply all the lazily stored queries
        self._update(start); self._update(stop - 1)
        while start < stop:
            if start & 1:
                res = min(res, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res = min(res, self.data[stop])
            start >>= 1; stop >>= 1
        return res

def DFS(graph, i, prev, subsizes, order, dists, d):
    ctr = 1
    order.append(i)
    dists.append(d)
    for j, w in graph[i]:
        if j != prev:
            ctr += DFS(graph, j, i, subsizes, order, dists, d + w)
    subsizes[i] = ctr
    return ctr

n = int(input())

graph = defaultdict(set)

edges = []

for _ in range(n - 1):
    u, v, w = map(int, input().split())
    edges.append([u, v, w])
    graph[u].add((v, w))
    graph[v].add((u, w))

stack = [(1, -1, 0)]

order = []

dists = []

subsizes = {}

DFS(graph, 1, -1, subsizes, order, dists, 0)

print(order, dists)

dists = LazySegmentTree(dists)

pos = {}

for i in range(n):
    pos[order[i]] = i

q = int(input())

for _ in range(q):
    a, b, c = map(int, input().split())
    if a == 1:
        u, v, w = edges[b - 1]
        u, v = sorted([u, v], key = lambda x: pos[x])
        dists.add(pos[v], pos[v] + subsizes[v] - 1, (1, c - w))
        edges[b - 1][2] = c
    if a == 2:
        print(dists.query(pos[b], pos[b] + 1) + dists.query(pos[c], pos[c] + 1) - 2 * dists.query(pos[b], pos[c] + 1))