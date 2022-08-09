t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    pos = [set() for __ in range(n)]
    for i in range(n):
        val = arr[i]
        pos[i].add(val)
        while val % 10 != 0:
            val += val % 10
            pos[i].add(val)
    res = set.intersection(*pos)
    if len(res) > 0:
        print("Yes")
    else:
        print("No")