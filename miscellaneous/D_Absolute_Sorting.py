t = int(input())

def valid(arr, n, x):
    for i in range(n - 1):
        if abs(arr[i] - x) > abs(arr[i + 1] - x):
            return False
    return True

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 1:
        print(0)
        continue
    lowest = float('-inf')
    highest = float('inf')
    for i in range(n - 1):
        if arr[i] < arr[i + 1]:
            highest = min(highest, (arr[i] + arr[i + 1]) // 2)
        if arr[i] > arr[i + 1]:
            lowest = max(lowest, (arr[i] + arr[i + 1]) // 2)
    if lowest == float('-inf'):
        print(min(arr))
    elif highest == float('inf'):
        print(max(arr))
    elif valid(arr, n, lowest):
        print(lowest)
    elif valid(arr, n, highest):
        print(highest)
    else:
        print(-1)