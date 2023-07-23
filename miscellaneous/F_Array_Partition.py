t = int(input())

def getrange(nums, n, cmp):
    stack = []
    nextpos = [n] * n
    prevpos = [-1] * n
    for i in range(n):
        while len(stack) > 0 and cmp(nums[i], nums[stack[-1]]):
            curr = stack.pop()
            nextpos[curr] = i
        if len(stack) > 0:
            prevpos[i] = stack[-1]
        stack.append(i)
    res = []
    for i in range(n):
        l = prevpos[i]
        r = nextpos[i]
        res.append((l + 1, r - 1))
    return res

def check(pos, mins, maxs):
    for el in pos:
        

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    maxs = getrange(arr, n, lambda a, b: a > b)
    mins = getrange(arr, n, lambda a, b: a < b)
    pos = {}
    for i in range(n):
        if arr[i] not in pos:
            pos[arr[i]] = []
        pos[arr[i]].append(i)
    print(check(pos, mins, maxs))