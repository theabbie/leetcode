t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    pa = [0] * (n + 1)
    pb = [0] * (n + 1)
    pc = [0] * (n + 1)
    for i in range(n):
        pa[i + 1] += pa[i] + a[i]
        pb[i + 1] += pb[i] + b[i]
        pc[i + 1] += pc[i] + c[i]
    