t = int(input())

def check(res):
    arr = sorted([a + b for a, b in res])
    n = len(arr)
    for i in range(n - 1):
        if arr[i + 1] - arr[i] != 1:
            return False
    return True

for _ in range(t):
    n = int(input())
    res = [[i, -1] for i in range(1, n + 1)]
    used = set()
    for i in range(n):
        if (i + 1) & 1:
            for x in range(2 * n, n, -1):
                if x not in used:
                    res[i][1] = x
                    used.add(x)
                    break
        else:
            for x in range(n + 1, 2 * n + 1):
                if x not in used:
                    res[i][1] = x
                    used.add(x)
                    break
    if check(res):
        print("Yes")
        print("\n".join(f"{a} {b}" for a, b in res))
    else:
        print("No")