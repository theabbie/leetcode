t = int(input())

def solve(arr, k):
    n = len(arr)
    diff = [max(arr[i] - arr[n - i - 1], 0) for i in range(n)]
    diff.sort(reverse = True)
    for _ in range(n - k):
        for i in range(k):
            diff[i] -= diff[k - 1]
        diff.sort(reverse = True)
    return diff[0] == 0

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print("YES" if solve(arr, k) else "NO")