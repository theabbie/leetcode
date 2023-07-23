t = int(input())

def solve(arr, n):
    nextsmaller = [n] * n
    nextgreater = [n] * n
    stack = []
    for i in range(n):
        while len(stack) > 0 and arr[i] > arr[stack[-1]]:
            prev = stack.pop()
            nextgreater[prev] = i
        stack.append(i)
    stack = []
    for i in range(n):
        while len(stack) > 0 and arr[i] < arr[stack[-1]]:
            prev = stack.pop()
            nextsmaller[prev] = i
        stack.append(i)
    for i in range(n):
        j = max(nextsmaller[i], nextgreater[i])
        if j < n:
            print(arr, i, j)
    return [-1]

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    print(*solve(p, n))