t = int(input())

def solve(arr, n):
    stack = []
    larger = [-1] * n
    smaller = [-1] * n
    largerright = [n] * n
    smallerright = [n] * n
    for i in range(n):
        while len(stack) > 0 and arr[stack[-1]] > arr[i]:
            curr = stack.pop()
            larger[i] = curr
        if len(stack) > 0:
            smaller[i] = stack[-1]
        stack.append(i)
    stack = []
    for i in range(n):
        while len(stack) > 0 and arr[i] > arr[stack[-1]]:
            curr = stack.pop()
            largerright[curr] = i
        if len(stack) > 0:
            smallerright[stack[-1]] = i
        stack.append(i)
    l = [-1] * n
    r = [n] * n
    for i in range(n):
        l[i] = min(smaller[i], larger[i])
        r[i] = max(smallerright[i], largerright[i])
    rmin = [None] * n
    rmin[0] = 0
    for i in range(1, n):
        if r[i] < r[rmin[i - 1]]:
            rmin[i] = i
        else:
            rmin[i] = rmin[i - 1]
    for i in range(n):
        if l[i] > -1 and i >= r[rmin[l[i]]]:
            print(rmin[l[i]] + 1, i + 1)
            return
    print(-1)
    return

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    solve(p, n)