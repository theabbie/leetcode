import math
from collections import Counter

def mos_algorithm(arr, queries, updateQueries):
    un = len(updateQueries)
    ui = 0
    block_size = int(math.sqrt(len(arr)))
    sorted_queries = sorted(enumerate(queries), key=lambda x: x[1][0] // block_size)
    left, right = 0, -1
    distvals = Counter()
    distsum = 0
    def remove(x):
        nonlocal distsum
        distvals[x] -= 1
        if distvals[x] == 0:
            distsum -= x
    def add(x):
        nonlocal distsum
        distvals[x] += 1
        if distvals[x] == 1:
            distsum += x
    results = [0] * len(queries)
    for query_index, (query_left, query_right, qpos) in sorted_queries:
        while 
        while left > query_left:
            left -= 1
            add(arr[left])
        while right < query_right:
            right += 1
            add(arr[right])
        while left < query_left:
            remove(arr[left])
            left += 1
        while right > query_right:
            remove(arr[right])
            right -= 1
        results[query_index] = distsum
    return results

n = int(input())

arr = list(map(int, input().split()))

q = int(input())

queries = []
updateQueries = []

for qpos in range(q):
    curr = input().split()
    if curr[0] == "Q":
        l, r = int(curr[1]) - 1, int(curr[2]) - 1
        queries.append((l, r, qpos))
    else:
        pos, v = int(curr[1]) - 1, int(curr[2])
        updateQueries.append((qpos, pos, v))

print("\n".join(map(str, mos_algorithm(arr, queries, updateQueries))))