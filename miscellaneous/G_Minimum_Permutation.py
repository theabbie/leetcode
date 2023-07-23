class SparseTable:
    def __init__(self, arr):
        n = len(arr)
        k = len("{:b}".format(n))
        table = [[(float("inf"), float('inf'))] * k for _ in range(n)]
        for l in range(k):
            for i in range(n):
                if l == 0:
                    table[i][l] = arr[i]
                else:
                    a = table[i][l - 1]
                    b = (float("inf"), float('inf'))
                    if i + (1 << l - 1) < n:
                        b = table[i + (1 << l - 1)][l - 1]
                    table[i][l] = min(a, b)
        self.table = table

    def min(self, l, r):
        bits = "{:b}".format(r - l)[::-1]
        res = (float("inf"), float('inf'))
        for i, b in enumerate(bits):
            if b == "1":
                res = min(res, self.table[l][i])
                l += 1 << i
        return res

n, m = map(int, input().split())

arr = list(map(int, input().split()))

pos = {}

for i in range(n):
    if arr[i] not in pos:
        pos[arr[i]] = []
    pos[arr[i]].append(i)

rmq = SparseTable([(arr[i], i) for i in range(n)])

res = []

a = 0
b = n - m

for i in range(m):
    val, j = rmq.min(a, b + 1)
    res.append(val)
    a = j + 1
    b += 1

print(*res)