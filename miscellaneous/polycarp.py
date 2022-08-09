from collections import defaultdict, deque

n = int(input())

arr = list(map(int, input().split()))

graph = defaultdict(list)

inorder = defaultdict(int)

arrset = set(arr)

for num in arr:
    if num * 2 in arrset:
        graph[num].append(num * 2)
        inorder[num * 2] += 1
    if num % 3 == 0 and num // 3 in arrset:
        graph[num].append(num // 3)
        inorder[num // 3] += 1

q = deque()

for num in arr:
    if inorder[num] == 0:
        q.appendleft(num)

res = []

while len(q) > 0:
    curr = q.pop()
    res.append(curr)
    for j in graph[curr]:
        inorder[j] -= 1
        if inorder[j] == 0:
            q.appendleft(j)

print(*res)