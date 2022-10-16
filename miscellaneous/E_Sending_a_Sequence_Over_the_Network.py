t = int(input())

def possible(arr, i, n, cache):
    if i == n:
        return True
    if i > n:
        return False
    if i in cache:
        return cache[i]
    if possible(arr, i + arr[i] + 1, n, cache):
        cache[i] = True
        return True
    for j in range(i + 1, n):
        if arr[j] == j - i and possible(arr, j + 1, n, cache):
            cache[i] = True
            return True
    cache[i] = False
    return False

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    valid = possible(arr, 0, n, {})
    if valid:
        print("YES")
    else:
        print("NO")