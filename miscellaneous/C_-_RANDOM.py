m, n = map(int, input().split())

a = []
b = []

for i in range(m):
    a.append(input())

for i in range(m):
    b.append(input())

aa = []
bb = []

for j in range(n):
    aa.append("".join(a[i][j] for i in range(m)))
    bb.append("".join(b[i][j] for i in range(m)))

print("Yes" if sorted(aa) == sorted(bb) else "No")