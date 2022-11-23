t = int(input())

for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    gsum = lambda s: sum(int(d) for d in s)
    asum, bsum = gsum(a), gsum(b)
    print(asum + bsum, n)