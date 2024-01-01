from sortedcontainers import SortedList

def mos_algorithm(arr, queries):
    block_size = int(math.sqrt(len(arr)))
    sorted_queries = sorted(enumerate(queries), key=lambda x: x[1][0] // block_size)
    left, right = 0, -1
    order = SortedList()
    diffs = [0] * (max(arr) - min(arr) + 1)
    ctr = 0
    def remove(x):
        nonlocal ctr
        i = order.bisect_left(x)
        p = 0
        old = 0
        for j in [i - 1, i + 1]:
            if 0 <= j < len(order):
                p += 1
                oldiff = abs(order[i] - order[j])
                diffs[oldiff] -= 1
                if diffs[oldiff] == 0:
                    ctr -= 1
                if j == i - 1:
                    old -= order[j]
                else:
                    old += order[j]
        if p == 2:
            diffs[old] += 1
            if diffs[old] == 1:
                ctr += 1
        order.pop(i)
    def add(x):
        nonlocal ctr
        order.add(x)
        i = order.bisect_left(x)
        p = 0
        old = 0
        for j in [i - 1, i + 1]:
            if 0 <= j < len(order):
                p += 1
                oldiff = abs(order[i] - order[j])
                diffs[oldiff] += 1
                if diffs[oldiff] == 1:
                    ctr += 1
                if j == i - 1:
                    old -= order[j]
                else:
                    old += order[j]
        if p == 2:
            diffs[old] -= 1
            if diffs[old] == 0:
                ctr -= 1
    results = [0] * len(queries)
    for query_index, (query_left, query_right) in sorted_queries:
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
        results[query_index] = ctr == 1
    return results

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        return mos_algorithm(nums, [(l[i], r[i]) for i in range(len(l))])