from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    res = []
    q = deque()
    for i in range(n):
        while len(q) > 0 and q[-1] <= i - k:
            q.pop()
        while len(q) > 0 and arr[i] > arr[q[0]]:
            q.popleft()
        q.appendleft(i)
        if i >= k - 1:
            res.append(arr[q[-1]])
    print(*res)