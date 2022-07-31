def DFS(i, N, B, v):
    if B[i - 1] not in v:
        v.add(B[i - 1])
        DFS(B[i - 1], N, B, v)

def solve(N, B):
    mnode = None
    msize = 0
    for i in range(1, N + 1):
        v = {i}
        DFS(i, N, B, v)
        if len(v) > msize:
            msize = len(v)
            mnode = i
    return mnode

N = int(input())

B = []

for _ in range(N):
    B.append(int(input()))

print(solve(N, B))