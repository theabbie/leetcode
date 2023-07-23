from collections import defaultdict
import math

t = int(input())

def mos_algorithm(arr, queries):
    block_size = int(math.sqrt(len(arr)))
    sorted_queries = sorted(enumerate(queries), key=lambda x: x[1][0] // block_size)
    left, right, distinct_count = 0, -1, 0
    minpower = 0
    powerleft = 0
    results = [0] * len(queries)
    for query_index, (query_left, query_right) in sorted_queries:
        while left > query_left:
            left -= 1
            if arr[left] > arr[left + 1]:
                minpower = max(minpower, arr[left])
            elif arr[left] == arr[left + 1] and arr[left] == minpower:
                minpower += 1
        while right < query_right:
            right += 1
            distinct_count += (frequency[arr[right]] == 0)
            frequency[arr[right]] += 1
        while left < query_left:
            if arr[left] > arr[left + 1]:
                minpower = max(minpower, arr[left])
            elif arr[left] == arr[left + 1] and arr[left] == minpower:
                minpower += 1
            left += 1
        while right > query_right:
            frequency[arr[right]] -= 1
            distinct_count -= (frequency[arr[right]] == 0)
            right -= 1
        results[query_index] = minpower
    return results

for _ in range(t):
    n, q = map(int, input().split())
    arr = map(int, input().split())
    queries = []
    for _ in range(q):
        l, r = map(int, input().split())
        queries.append((l - 1, r - 1))
    print("\n".join(map(str, mos_algorithm(arr, queries))))