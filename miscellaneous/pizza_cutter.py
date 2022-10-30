t = int(input())

for _ in range(t):
    arr = list(map(int, input().split()))
    cuts = set()
    n = arr[0]
    for i in range(1, n + 1):
        ang = abs(arr[i]) % 360
        if arr[i] < 0:
            ang = 360 - ang
        ang = ang % 180
        cuts.add(ang)
    k = len(cuts)
    if k == 0:
        print(1)
    else:
        print(2 * k)