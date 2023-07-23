t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    pos = False
    for parity in range(2):
        currpos = True
        ctr = [0] * 2
        i = 0
        for el in arr:
            while i < n and arr[i] < el:
                ctr[arr[i] % 2] += 1
                i += 1
            if el % 2 != parity and ctr[(parity + el) % 2] == 0:
                currpos = False
                break
        if currpos:
            pos = True
            break
    print("YES" if pos else "NO")