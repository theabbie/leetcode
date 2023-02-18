from collections import defaultdict, Counter, deque
import math
import heapq
import bisect
import sys

sys.setrecursionlimit(10 ** 6)

M = 10 ** 9 + 7

primes = []
smallestprimefactor = []
factorial = []
factorialinv = []

def accumulate(arr, init, fn):
    for el in arr:
        init = fn(init, el)
    return init

class Number:
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    def lcm(a, b):
        return a * b // Number.gcd(a, b)
    
    def isPrime(N):
        i = 2
        while i * i <= N:
            if N % i == 0:
                return False
            i += 1
        return True
    
    def SQRT(N):
        end = 1
        while end * end < N:
            end *= 2
        beg = end // 2
        res = 1
        while beg <= end:
            mid = (beg + end) // 2
            if mid * mid <= N:
                res = mid
                beg = mid + 1
            else:
                end = mid - 1
        return res
    
    def factorial(N):
        factorial.extend([1] * (N + 1))
        factorialinv.extend([1] * (N + 1))
        for i in range(1, N + 1):
            factorial[i] *= factorial[i - 1]
            factorial[i] % M
        factorialinv[N] = pow(factorial[N], M - 2, M)
        for i in range(N - 1, -1, -1):
            factorialinv[i] = (i + 1) * factorialinv[i + 1]
            factorialinv[i] %= M
    
    def sieve(N):
        primes.extend([True] * (N + 1))
        primes[0] = primes[1] = False
        i = 0
        while i * i <= N:
            if primes[i]:
                smallestprimefactor[i] = i
                j = i * i
                while j <= N:
                    primes[j] = False
                    j += i
            i += 1
    
    def listofprimes():
        primelist = []
        for i in range(len(primes)):
            if primes[i]:
                primelist.append(i)
        return primelist
    
    def primepowers(N, p, mod):
        ip = mod(p, mod - 2, mod)
        pw = 1
        invpw = 1
        ppow = []
        invppow = []
        for _ in range(n):
            ppow.append(pw)
            invppow.append(invpw)
            pw = (pw * p) % mod
            invpw = (invpw * ip) % mod
        return ppow, invppow
    
    def comb(N, K):
        return (factorial[N] * factorialinv[K] * factorialinv[N - k]) % M
    
    def perm(N, K):
        return (factorial[N] * factorialinv[N - k]) % M
    
class Graph:
    def __init__(self):
        self.graph = defaultdict(set)
        self.nodes = set()
        self.indegree = Counter()
        
    def DFS(self, root, visited):
        stack = deque([root])
        while len(stack) > 0:
            curr = stack.pop()
            for j, w in self.graph[curr]:
                if j not in v:
                    v.add(j)
                    stack.append(j)
                    
    def BFS(self, root, visited):
        q = deque([root])
        while len(q) > 0:
            curr = stack.pop()
            for j, w in self.graph[curr]:
                if j not in v:
                    v.add(j)
                    q.appendleft(j)
            
class DirectedGraph(Graph):
    def add(a, b, w = 1):
        self.graph[a].add((b, w))
        self.nodes.add(a)
        self.nodes.add(b)
        self.indegree[b] += 1
        
    def toposort(self):
        res = []
        q = deque()
        dec = Counter()
        for node in self.nodes:
            if self.indegree[node] == 0:
                q.appendleft(node)
        while len(q) > 0:
            curr = q.pop()
            res.append(curr)
            for j, w in self.graph[curr]:
                dec[j] += 1
                if self.indegree[j] - dec[j] == 0:
                    q.appendleft(j)
        return res
        
class UndirectedGraph(Graph):
    def add(self, a, b, w = 1):
        self.graph[a].add((b, w))
        self.graph[b].add((a, w))
        self.nodes.add(a)
        self.nodes.add(b)
        self.indegree[a] += 1
        self.indegree[b] += 1
        
class Tree(Graph):
    def DFS(self, root):
        stack = deque([(root, -1)])
        while len(stack) > 0:
            curr, prev = stack.pop()
            for j, w in self.graph[curr]:
                if j != prev:
                    stack.append(j)
                    
    def BFS(self, root):
        q = deque([(root, -1)])
        while len(q) > 0:
            curr = stack.pop()
            for j, w in self.graph[curr]:
                if j != prev:
                    q.appendleft(j)
                    
class PolyHash:
    def __init__(self, arr, p, mod):
        self.mod = mod
        self.hashvals = self.hashes(arr)
        self.overall = self.hashvals[-1]
        self.ppow, self.invppow = Number.primepowers(N + 1, p, mod)
        self.queue = deque(arr)
        
    def hashes(self, arr):
        n = len(arr)
        h = [0] * (n + 1)
        for i in range(n):
            h[i + 1] = (h[i] + self.ppow[i] * arr[i]) % self.mod
        return h
    
    def appendleft(self, val):
        n = len(self.queue)
        self.queue.appendleft(val)
        self.overall -= self.pop() * self.ppow[n - 1]
        self.overall = (val + self.mod * self.overall) % self.mod
        
    def update(self, index, inc):
        self.overall += inc * self.ppow[index]
        self.overall %= self.mod
        
    def rangeHash(self, i, j):
        return self.invppow[i] * (self.hashvals[j + 1] + self.mod - self.hashvals[i])
    
class String:
    def LCP(s):
        g, pi = 0, [0] * len(s)
        for i in range(1, len(s)):
            while g and (s[g] != s[i]):
                g = pi[g - 1]
            pi[i] = g = g + (s[g] == s[i])
        return pi
    
    def z_function(S):
        n = len(S)
        Z = [0] * n
        l = r = 0
        for i in range(1, n):
            z = Z[i - l]
            if i + z >= r:
                z = max(r - i, 0)
                while i + z < n and S[z] == S[i + z]:
                    z += 1
                l, r = i, i + z
            Z[i] = z
        Z[0] = n
        return Z
    
class DSU:
    def __init__(self):
        self.parent = defaultdict(lambda x: x)
        self.size = defaultdict(lambda: 1)
        
    def find(self, a):
        if a == self.parent[a]:
            return a
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
        
    def union(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)
        if parent_a != parent_b:
            if self.size[parent_a] < self.size[parent_b]:
                parent_a, parent_b = parent_b, parent_a
            self.parent[parent_b] = parent_a
            self.size[parent_a] += self.size[parent_b]
            
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
    
class SegTreeNode:
    def __init__(self, val):
        self.val = val
    
class SegTree:
    def __init__(self, arr, func, init):
        self.nodes = defaultdict(lambda: SegTreeNode(init))
        self.func = func
        self.init = init
        self.beg = 0
        self.end = len(arr)
        for i, val in enumerate(arr):
            self.update(i, val)

    def query(self, a, b, x = 0, y = None, k = 1):
        if y == None:
            y = self.end
        if b < x or a > y:
            return self.init
        if a <= x and b >= y:
            return self.nodes[k].val
        mid = (x + y) // 2
        l = self.query(a, b, x, mid, 2 * k)
        r = self.query(a, b, mid + 1, y, 2 * k + 1)
        return self.func(l, r)
    
    def update(self, i, val, x = 0, y = None, k = 1):
        if y == None:
            y = self.end
        if x == y:
            self.nodes[k].val = val
            return
        mid = (x + y) // 2
        if i <= mid:
            self.update(i, val, x, mid, 2 * k)
        else:
            self.update(i, val, mid + 1, y, 2 * k + 1)
        self.nodes[k].val = self.func(self.nodes[2 * k].val, self.nodes[2 * k + 1].val)
    
class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False
        self.ctr = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s):
        curr = self.root
        curr.ctr += 1
        for c in s:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
            curr.ctr += 1
        curr.end = True

    def getAll(self, node=None):
        node = node or self.root
        res = []
        if node.end:
            res.append("")
        for c in node.child:
            res.extend([c + s for s in self.getAll(node.child[c])])
        return res

    def check(self, s):
        curr = self.root
        for c in s:
            if c not in curr.child:
                return None
            curr = curr.child[c]
        return curr

    def startswith(self, s):
        res = self.check(s)
        if not res:
            return []
        return [s + suffix for suffix in self.getAll(res)]

    def exists(self, s):
        res = self.check(s)
        return res and res.end
    
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    fw = FenwickTree([0] * (max(arr) + 1))
    inv = 0
    for i in range(n - 1, -1, -1):
        inv += fw.query(arr[i] + 1)
        fw.update(arr[i], 1)
    res = inv
    rctr = Counter(arr)
    lctr = Counter()
    currdec = 0
    for el in arr:
        lctr[el] += 1
        rctr[el] -= 1
        currdec += rctr[el - 1]
        currdec -= lctr[el + 1]
        res = min(res, inv - currdec)
    print(inv - res)

SINGLE = False

t = 1

if not SINGLE:
    t = int(input())

for _ in range(t):
    solve()