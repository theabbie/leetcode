import math
from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 7)

def mos_algorithm(arr, queries):
    block_size = int(math.sqrt(len(arr)))
    sorted_queries = sorted(enumerate(queries), key=lambda x: x[1][0] // block_size)
    left, right, distinct_count = 0, -1, 0
    frequency = defaultdict(int)
    results = [0] * len(queries)
    for query_index, (query_left, query_right) in sorted_queries:
        while left > query_left:
            left -= 1
            distinct_count += (frequency[arr[left]] == 0)
            frequency[arr[left]] += 1
        while right < query_right:
            right += 1
            distinct_count += (frequency[arr[right]] == 0)
            frequency[arr[right]] += 1
        while left < query_left:
            frequency[arr[left]] -= 1
            distinct_count -= (frequency[arr[left]] == 0)
            left += 1
        while right > query_right:
            frequency[arr[right]] -= 1
            distinct_count -= (frequency[arr[right]] == 0)
            right -= 1
        results[query_index] = distinct_count
    return results

def euler_tour(graph):
    tour = []
    def dfs(node, prev):
        tour.append(node)
        for neighbor in graph[node]:
            if neighbor != prev:
                dfs(neighbor, node)
                tour.append(node)
    dfs(0, -1)
    return tour

n = int(input())

arr = list(map(int, input().split()))

graph = defaultdict(set)

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u - 1].add(v - 1)
    graph[v - 1].add(u - 1)

tour = euler_tour(graph)

first = {}
last = {}

for i in range(len(tour)):
    if tour[i] not in first:
        first[tour[i]] = i
    last[tour[i]] = i

print(*mos_algorithm([arr[i] for i in tour], [[first[i], last[i]] for i in range(n)]))