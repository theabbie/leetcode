import math
from collections import defaultdict

def mos_algorithm(arr, queries):
    block_size = int(math.sqrt(len(arr)))
    sorted_queries = sorted(enumerate(queries), key = lambda x: x[1][0] // block_size)
    left, right, val = 0, -1, 0
    frequency = defaultdict(int)
    results = [0] * len(queries)
    for query_index, (query_left, query_right) in sorted_queries:
        while left > query_left:
            left -= 1
            val += frequency[arr[left]] * (frequency[arr[left]] - 1) // 2
            frequency[arr[left]] += 1
        while right < query_right:
            right += 1
            val += frequency[arr[right]] * (frequency[arr[right]] - 1) // 2
            frequency[arr[right]] += 1
        while left < query_left:
            frequency[arr[left]] -= 1
            val -= frequency[arr[left]] * (frequency[arr[left]] - 1) // 2
            left += 1
        while right > query_right:
            frequency[arr[right]] -= 1
            val -= frequency[arr[right]] * (frequency[arr[right]] - 1) // 2
            right -= 1
        results[query_index] = val
    return results

n, q = map(int, input().split())

arr = list(map(int, input().split()))

queries = []

for _ in range(q):
    l, r = map(int, input().split())
    queries.append((l - 1, r - 1))

print("\n".join(map(str, mos_algorithm(arr, queries))))