t = int(input())

def count(x, y, n):
    return (n - y) // 2

for _ in range(t):
    n = int(input())
    x, y = map(int, input().split())
    k = (n + 1) // 2
    if y > n - 2 * abs(k - x):
        print(-1)
        continue 
    i = count(x, y, n)
    j = count(x, n - 2 * abs(k - x) + 1 - y, n)
    print(1 + i + j)