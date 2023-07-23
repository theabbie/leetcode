n = int(input())

arr = list(map(int, input().split()))

seen = [0] * n

f = [-1] * n

for i in range(3 * n):
    seen[arr[i] - 1] += 1
    if seen[arr[i] - 1] == 2:
        f[arr[i] - 1] = i

print(*sorted(range(1, n + 1), key = lambda x: f[x - 1]))