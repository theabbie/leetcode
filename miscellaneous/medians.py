t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    arr = map(int, input().split())
    arr.sort(reverse = True)
    maxsum = 0
    for i in range(min(m - 1, n)):
        maxsum += arr[i]
    rem = arr[min(m - 1, n):]
    k = len(rem)
    if k % 2 == 1:
        maxsum += rem[(k + 1) // 2]
    elif k > 0:
        maxsum += (rem[(k - 1) // 2] + rem[k // 2]) / 2
    print(maxsum)
