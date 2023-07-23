from collections import deque

n = int(input())

arr = list(map(int, input().split()))

for i in range(n):
    arr[i] -= 1

cycle = [float('inf')] * n

indegree = [0] * n

for i in range(n):
    indegree[arr[i]] += 1

q = deque()

for i in range(n):
    if indegree[i] == 0:
        q.appendleft(i)

visited = set(range(n))

while len(q) > 0:
    curr = q.pop()
    visited.remove(curr)
    indegree[arr[curr]] -= 1
    if indegree[arr[curr]] == 0:
        q.appendleft(arr[curr])

for i in visited:
    ctr = 1
    curr = arr[i]
    while curr != i:
        curr = arr[curr]
        ctr += 1
    cycle[i] = ctr
    curr = arr[i]
    while curr != i:
        cycle[curr] = ctr
        curr = arr[curr]
        ctr += 1

print(cycle)