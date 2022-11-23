t = int(input())

for _ in range(t):
    n, c, d = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse = True)
    total = sum(arr)
    p = c // total
    if c % total != 0:
        p += 1
    i = 0
    curr = 0
    used = 0
    while i < n and curr < c:
        curr += p * arr[i]
        used += p
        if curr > c:
            used -= (curr - c) // arr[i]
            if (curr - c) % arr[i] != 0:
                used -= 1
        i += 1
    if used > d:
        print("Impossible")
    else:
        print(curr, p)