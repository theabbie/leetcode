t = int(input())

def area(d, h, hh):
    return (0.5 * d * hh * hh) / h

for _ in range(t):
    n, d, h = map(int, input().split())
    trees = list(map(int, input().split()))
    trees.sort()
    res = 0
    for i in range(n):
        res += area(d, h, h)
        if i < n - 1 and trees[i] + h > trees[i + 1]:
            res -= area(d, h, trees[i] + h - trees[i + 1])
    print(int(res * 10000000) / 10000000)