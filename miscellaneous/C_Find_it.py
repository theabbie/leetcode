def longestCycle(edges):
    n = len(edges)
    res = []
    v = set()
    for node in range(n):
        i = 0
        pos = {}
        curr = []
        while node != -1 and node not in v:
            pos[node] = i
            curr.append(node + 1)
            v.add(node)
            node = edges[node]
            i += 1
        if node != -1 and node in pos:
            curr.reverse()
            while len(curr) > 0 and curr[-1] != node + 1:
                curr.pop()
            curr.reverse()
            if len(curr) > len(res):
                res = curr
    return res

n = int(input())

arr = list(map(int, input().split()))

for i in range(n):
    arr[i] -= 1

res = longestCycle(arr)

print(len(res))

print(*res)