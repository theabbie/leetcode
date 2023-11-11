from collections import defaultdict
import sys

sys.setrecursionlimit(2 * 10 ** 5)

n = int(input())

graph = defaultdict(set)

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a - 1].add(b - 1)
    graph[b - 1].add(a - 1)
    
