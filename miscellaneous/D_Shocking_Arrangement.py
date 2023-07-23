from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    q = deque(arr)
    k = arr[-1] - arr[0]
    maxendinghere = float('-inf')
    minendinghere = float('inf')
    res = []
    for i in range(n):
        for pos, j in [(q[0], 0), (q[-1], 1)]:
            newmaxendinghere = max(pos, pos + maxendinghere)
            newminendinghere = min(pos, pos + minendinghere)
            if newmaxendinghere < k and newminendinghere > -k:
                res.append(pos)
                if j == 0:
                    q.popleft()
                else:
                    q.pop()
                maxendinghere = newmaxendinghere
                minendinghere = newminendinghere
                break
    if len(res) == n:
        print("Yes")
        print(*res)
    else:
        print("No")